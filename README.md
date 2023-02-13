# CRCSet
`CRCSet` aims to provide `crc` implementation for python.

### What's the difference with other packages?
With the integrated `WASI` and `WASM` modules, this package eliminates the hassle of platform-specific compilations. Simply install the package and start using it. The package initially utilizes the `wasmer` runtime for execution, but in the case it's not available, it provides a reliable fallback option with `pywasm`, a pure Python-based `WASM` runtime.

## Usage
1. Install the library:
    ```sh
    pip install crcset
    ```
2. Use it:
   ```python
   from crcset import crc32c, crc16xmodem
   print(crc32c(b"testing-crc32c")) # 4017753803
   print(crc16xmodem(b"testing-crc16-xmodem")) # 26763
   ```