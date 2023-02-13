import sys
from pathlib import Path

from pywasm import Runtime

from crcset.wasm.wasm import byte_alloc, open_instance


class CRCSet:
    _instance: Runtime = None

    @classmethod
    def _get_instance(cls) -> Runtime:
        if cls._instance is None:
            p = Path(sys.modules["crcset"].__file__).parent
            p = p.joinpath("wasm/_crcset_wasm.wasm")
            cls._instance = open_instance(p)
        return cls._instance

    @classmethod
    def crc32c(cls, data: bytes) -> int:
        ins = cls._get_instance()
        pointer, ln = byte_alloc(ins, "alloc", data)
        return ins.exec("crc32", [pointer, ln]) & 0xFFFFFFFF

    @classmethod
    def crc16xmodem(cls, data: bytes) -> int:
        ins = cls._get_instance()
        pointer, ln = byte_alloc(ins, "alloc", data)
        return ins.exec("crc16", [pointer, ln]) & 0xFFFF


crc32c = CRCSet.crc32c
crc16xmodem = CRCSet.crc16xmodem
