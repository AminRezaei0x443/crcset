import sys
from pathlib import Path

from wasmer import Instance

from crcset.wasi.wasi import byte_alloc, open_instance


class CRCSet:
    _instance: Instance = None

    @classmethod
    def _get_instance(cls) -> Instance:
        if cls._instance is None:
            p = Path(sys.modules["crcset"].__file__).parent
            p = p.joinpath("wasi/_crcset_wasi.wasm")
            cls._instance = open_instance(p)
        return cls._instance

    @classmethod
    def crc32c(cls, data: bytes) -> int:
        ins = cls._get_instance()
        pointer, ln = byte_alloc(ins.exports.memory, ins.exports.alloc, data)
        return ins.exports.crc32(pointer, ln) & 0xFFFFFFFF

    @classmethod
    def crc16xmodem(cls, data: bytes) -> int:
        ins = cls._get_instance()
        pointer, ln = byte_alloc(ins.exports.memory, ins.exports.alloc, data)
        return ins.exports.crc16(pointer, ln) & 0xFFFF


crc32c = CRCSet.crc32c
crc16xmodem = CRCSet.crc16xmodem
