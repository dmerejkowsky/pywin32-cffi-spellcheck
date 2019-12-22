import sys
from setuptools import setup, find_packages

if sys.version_info.major < 3:
    sys.exit("Error: Please upgrade to Python3")


def get_long_description() -> str:
    with open("README.rst") as fp:
        return fp.read()


setup(
    name="pywin32-cffi-spellcheck",
    version="0.1",
    description="cffi bindings for Spellcheck.h on Windows",
    long_description = get_long_description(),
    url="https://github.com/pyenchant/pywin32-cffi-spellcheck",
    author="Dimitri Merejkowsky",
    packages=find_packages(),
    setup_requires=[
        # To run build_spellcheck.py
        "cffi>=1.12",
    ],
    cffi_modules=["build_spellcheck.py:ffibuilder"],
    install_requires=["cffi>=1.12"],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
