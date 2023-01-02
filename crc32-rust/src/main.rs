fn main() {
    println!("CRC32C - WASI");
}

#[no_mangle]
pub extern "C" fn crc32(data: *const u8, len: usize) -> u32 {
    unsafe{
        let msg = std::slice::from_raw_parts(data, len);
        let crc = crc32c::crc32c(msg);
        crc
    }
}

#[no_mangle]
pub fn alloc(len: usize) -> *mut u8 {
    // SRC: https://radu-matei.com/blog/practical-guide-to-wasm-memory/
    let mut buf = Vec::with_capacity(len);
    let ptr = buf.as_mut_ptr();
    std::mem::forget(buf);
    return ptr;
}