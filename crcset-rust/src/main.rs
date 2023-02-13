use crc::{Crc, CRC_32_ISCSI};

pub const CASTAGNOLI: Crc<u32> = Crc::<u32>::new(&CRC_32_ISCSI);

fn main() {
    println!("CRCSET - WASI");
}

#[no_mangle]
pub extern "C" fn crc32(data: *const u8, len: usize) -> u32 {
    unsafe{
        let msg = std::slice::from_raw_parts(data, len);
        let crc = CASTAGNOLI.checksum(msg);
        crc
    }
}

#[no_mangle]
pub extern "C" fn crc16(data: *const u8, len: usize) -> u16 {
    unsafe{
        let msg = std::slice::from_raw_parts(data, len);
        let crc = crc16::State::<crc16::XMODEM>::calculate(msg);
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