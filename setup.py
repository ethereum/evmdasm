#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version="0.1.0"

setup(
    name="evm-instructions",
    version=version,
    packages=find_packages(),
    author="tintinweb",
    author_email="tintinweb@oststrom.com",
    description=(
        "A lightweight object-oriented ethereum evm bytecode asm instruction registry and disassembler library."),
    license="GPLv2",
    keywords=["ethereum", "blockchain", "evm", "disassembler"],
    url="https://github.com/tintinweb/evm-instructions",
    download_url="https://github.com/tintinweb/evm-instructions/tarball/v%s"%version,
    #python setup.py register -r https://testpypi.python.org/pypi
    long_description=read("README.md") if os.path.isfile("README.md") else "",
    long_description_type='text/markdown',
    install_requires=[""],
    #package_data={},
    #extras_require={},
)
