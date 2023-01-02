from wasmer import engine, wasi, Store, Module, ImportObject, Instance
from wasmer_compiler_cranelift import Compiler


wasm_bytes = open("target/wasm32-wasi/release/crc32c.wasm", "rb").read()
# wasm_bytes = open("target\wasm32-wasi\debug\crc32c.wasm", "rb").read()
store = Store(engine.Universal(Compiler))
module = Module(store, wasm_bytes)
wasi_version = wasi.get_version(module, strict=True)

wasi_env = wasi.StateBuilder('wasi_test_program').finalize()
import_object = wasi_env.generate_import_object(store, wasi_version)
instance = Instance(module, import_object)

instance.exports._start()

b_data = "madareto-gaiidam...".encode("utf-8")
pointer = instance.exports.alloc(len(b_data))
memory = instance.exports.memory.uint8_view(offset=pointer)
for i in range(len(b_data)):
    memory[i] = b_data[i]

crc = instance.exports.crc32(pointer, len(b_data)) & 0xffffffff
print(crc)