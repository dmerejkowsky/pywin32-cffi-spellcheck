from cffi import FFI

ffibuilder = FFI()
from path import Path

ffibuilder.cdef(Path("cffi_defs.h").text())
ffibuilder.set_source(
    "_spellcheck",
    Path("cffi_src.cpp").text(),
    source_extension=".cpp",
    libraries=["ole32"],
    language="c++",
)


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
