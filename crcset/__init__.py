try:
    # Use wasmer wherever available
    import wasmer
    backend = "WASI"
except ImportError:
    # Wasmer is not available
    backend = "WASM"

if backend == "WASM":
    from crcset.crcset_wasm import crc16xmodem, crc32c
elif backend == "WASI":
    from crcset.crcset_wasi import crc16xmodem, crc32c
else:
    raise RuntimeError("Unknown backend!")

__all__ = [
    "crc32c",
    "crc16xmodem",
]
