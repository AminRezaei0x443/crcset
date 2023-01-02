from wasmer import Function, Instance, Module, Store, engine, wasi
from wasmer_compiler_cranelift import Compiler


def open_instance(wasi_file: str) -> Instance:
    with open(wasi_file, "rb") as f:
        wasm_bytes = f.read()

    store = Store(engine.Universal(Compiler))
    module = Module(store, wasm_bytes)
    wasi_version = wasi.get_version(module, strict=True)

    wasi_env = wasi.StateBuilder("_wasi_program").finalize()
    import_object = wasi_env.generate_import_object(store, wasi_version)
    instance = Instance(module, import_object)
    return instance


def byte_alloc(memory, alloc_fn: Function, data: bytes) -> tuple[int, int]:
    ln = len(data)
    pointer = alloc_fn(ln)
    memory = memory.uint8_view(offset=pointer)
    for i in range(ln):
        memory[i] = data[i]
    return pointer, ln
