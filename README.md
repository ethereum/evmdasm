[![Build Status](https://api.travis-ci.org/tintinweb/evmdasm.svg?branch=master)](https://travis-ci.org/tintinweb/evmdasm/)

# evmdasm
*A lightweight ethereum evm bytecode instruction registry, disassembler and evmcode manipulation library.*

This library is meant for providing a static interface and registry for EVM opcodes and instructions. The idea is to keep it as lightweight as possible especially when it comes to dependencies or high level features.

e.g. The [ethereum-dasm](https://github.com/tintinweb/ethereum-dasm) project - a kind of high level disassembler with static/dynamic analysis features - relies on the registry and base disassembling functionality provided by [evmdasm](https://github.com/tintinweb/evmdasm). 


**More information** --> **[Wiki](https://github.com/tintinweb/evmdasm/wiki)**

Projects building on [evmdasm](https://github.com/tintinweb/evmdasm/):
* :trophy: https://github.com/ethereum/evmlab/
* :trophy: https://github.com/tintinweb/ethereum-dasm
* :trophy: https://github.com/tintinweb/evmcodegen

### Setup

##### from pypi
```
#> python3 -m pip install evmdasm
```

##### from source
```
#> python3 setup.py install
```
