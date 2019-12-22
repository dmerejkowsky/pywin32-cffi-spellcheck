from cffi import FFI

ffibuilder = FFI()


def read_defs():
    with open("cffi_defs.h", "r") as f:
        return f.read()


def read_sources():
    with open("cffi_src.cpp", "r") as f:
        return f.read()


ffibuilder.cdef(read_defs())
ffibuilder.set_source(
    "_spellcheck",
    read_sources(),
    source_extension=".cpp",
    libraries=["ole32"],
    language="c++",
)


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
