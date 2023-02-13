from pywasm import load, Runtime


def open_instance(wasm_file: str) -> Runtime:
    runtime = load(wasm_file)
    return runtime


def byte_alloc(runtime: Runtime, alloc_fn: str, data: bytes) -> tuple[int, int]:
    ln = len(data)
    pointer = runtime.exec(alloc_fn, [ln])
    runtime.store.memory_list[0].data[pointer: pointer + ln] = data
    return pointer, ln
