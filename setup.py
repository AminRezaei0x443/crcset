import os
import shutil
from distutils.errors import CompileError
from subprocess import call

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py


# Thanks to: https://www.ardanlabs.com/blog/2020/08/packaging-python-code.html
class build_wasi_ext(build_py):
    """Customized build command to build rust module as WASI."""

    def run(self):
        wasi_path = os.path.join(os.getcwd(), "crcset/wasi/_crcset_wasi.wasm")
        wasm_path = os.path.join(os.getcwd(), "crcset/wasm/_crcset_wasm.wasm")
        od = os.getcwd()
        td = os.path.join(os.getcwd(), "crcset-rust")
        os.chdir(td)
        # Build WASI
        cmd = ["cargo", "wasi", "build", "--release"]
        out = call(cmd)
        # Build WASM (Fallback option)
        cmd = ["cargo", "build", "--target", "wasm32-unknown-unknown", "--release"]
        out_w = call(cmd)
        os.chdir(od)
        binary_path = os.path.join(
            os.getcwd(), "crcset-rust/target/wasm32-wasi/release/crcset.wasm",
        )
        binary_path_w = os.path.join(
            os.getcwd(), "crcset-rust/target/wasm32-unknown-unknown/release/crcset.wasm",
        )
        shutil.copy(binary_path, wasi_path)
        shutil.copy(binary_path_w, wasm_path)
        if out != 0:
            raise CompileError("Rust WASI build failed")
        if out_w != 0:
            raise CompileError("Rust WASI build failed")
        super(build_py, self).run()


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="crcset",
    version="0.0.4",
    description="",
    license="MIT",
    packages=find_packages(),
    author="Amin Rezaei",
    author_email="AminRezaei0x443@gmail.com",
    keywords=[],
    url="https://github.com/AminRezaei0x443/crcset",
    install_requires=required,
    extras_require={},
    package_data={
        "crcset.wasi": [
            "_crcset_wasi.wasm",
        ],
        "crcset.wasm": [
            "_crcset_wasm.wasm",
        ],
    },
    cmdclass={"build_py": build_wasi_ext},
    zip_safe=False,
)
