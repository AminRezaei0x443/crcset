# CRCSet
`CRCSet` aims to provide `crc` implementation for python.

### What's the difference with other packages?
This package has builtin `WASI` module and there is no need to compile for each platform. Just install the package and enjoy it.

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