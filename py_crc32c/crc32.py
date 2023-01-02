import sys
from pathlib import Path

from wasmer import Instance

from py_crc32c.wasi.wasi import byte_alloc, open_instance


class CRC32C:
    _instance: Instance = None

    @classmethod
    def _get_instance(cls) -> Instance:
        if cls._instance is None:
            p = Path(sys.modules["py_crc32c"].__file__).parent
            p = p.joinpath("wasi/_crc32_wasi.wasm")
            cls._instance = open_instance(p)
        return cls._instance

    @classmethod
    def crc32c(cls, data: bytes) -> int:
        ins = cls._get_instance()
        pointer, ln = byte_alloc(ins.exports.memory, ins.exports.alloc, data)
        return ins.exports.crc32(pointer, ln) & 0xFFFFFFFF


crc32c = CRC32C.crc32c
