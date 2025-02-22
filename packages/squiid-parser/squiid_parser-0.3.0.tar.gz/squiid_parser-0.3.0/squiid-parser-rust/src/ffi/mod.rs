use std::{
    ffi::{CStr, CString, NulError},
    mem,
    os::raw::{c_char, c_int},
};

use crate::parse;

mod cleanup;
mod version;

/// Structure containing the result of a parse operation done over FFI. Will contain either a
/// result array or an error message, but not both.
#[repr(C)]
#[derive(Debug, Clone)]
struct ParseResultFFI {
    /// The array of strings if the result was a success, else null
    result: *mut *mut c_char,
    /// The length of the result array
    result_len: c_int,
    /// The error message if an error was encountered, else null
    error: *mut c_char,
}

impl ParseResultFFI {
    /// Construct a new successful ParseResultFFI
    fn new(result: *mut *mut c_char, result_len: c_int) -> Self {
        Self {
            result,
            result_len,
            error: std::ptr::null_mut(),
        }
    }

    /// Construct a new ParseResultFFI with an error message
    fn new_error(error: &str) -> Self {
        let raw_error = CString::new(error).unwrap().into_raw();
        Self {
            result: std::ptr::null_mut(),
            result_len: 0,
            error: raw_error,
        }
    }
}

/// Parse a given algebraic (infix) notation string into an array of RPN (postfix) commands.
///
/// # Arguments
///
/// * `input` - The string input to parse
#[no_mangle]
#[deny(clippy::unwrap_used, clippy::expect_used, clippy::panic)]
extern "C" fn parse_exposed(input: *const c_char) -> ParseResultFFI {
    let c_str = unsafe { CStr::from_ptr(input) };
    let input_string = match c_str.to_str() {
        Ok(v) => v,
        Err(_) => return ParseResultFFI::new_error("Invalid UTF-8 string"),
    };

    let parsed_input = match parse(input_string) {
        Ok(v) => v,
        Err(e) => return ParseResultFFI::new_error(&e),
    };

    // Convert parsed input to Vec<CString>
    let c_strings: Result<Vec<CString>, NulError> =
        parsed_input.into_iter().map(|s| CString::new(s)).collect();

    let c_strings = match c_strings {
        Ok(v) => v,
        Err(_) => {
            return ParseResultFFI::new_error(&format!(
                "found invalid string data when converting data to a string",
            ))
        }
    };

    // Turning each null-terminated string into a pointer.
    // `into_raw` takes ownershop, gives us the pointer and does NOT drop the data.
    let mut out = c_strings
        .into_iter()
        .map(|s| s.into_raw())
        .collect::<Vec<_>>();

    out.shrink_to_fit();
    assert!(out.len() == out.capacity());

    // get the pointer to the vector
    let len = out.len();
    let vec_ptr = out.as_mut_ptr();
    mem::forget(out);

    ParseResultFFI::new(vec_ptr, len as c_int)
}
