[![Build Status](https://api.travis-ci.org/tintinweb/evmdasm.svg?branch=master)](https://travis-ci.org/tintinweb/evmdasm/)

# evmdasm
*A lightweight ethereum evm bytecode instruction registry and disassembler library.*

This library is meant for providing a static interface and registry for EVM opcodes and instructions. The idea is to keep it as lightweight as possible especially when it comes to dependencies or high level features.

e.g. The [ethereum-dasm](https://github.com/tintinweb/ethereum-dasm) project - a kind of high level disassembler with static/dynamic analysis features - relies on the registry and base disassembling functionality provided by [evmdasm](https://github.com/tintinweb/evmdasm). 


For more information visit the [Wiki](https://github.com/tintinweb/evmdasm/wiki)

### Setup

##### from pypi
```
#> python3 -m pip install evmdasm
```

##### from source
```
#> python3 setup.py install
```

### Commandline Utility

#### usage
```
#> python3 -m evmdasm --help
```

#### disassemble
```
#> echo 60406040ff | python3 -m evmdasm --disassemble
#> python3 -m evmdasm --disassemble 0x60406040ff
PUSH1 40
PUSH1 40
SELFDESTRUCT
```

#### list available instructions
```
#> python3 -m evmdasm --list [<filter>]
0xop | instruction          category             gas
============================================================
0x0  | STOP                 terminate            0
0x1  | ADD                  arithmetic           3
0x2  | MUL                  arithmetic           5
0x3  | SUB                  arithmetic           3
...
0xf0 | CREATE               system               32000
0xf1 | CALL                 system               40
0xf2 | CALLCODE             system               40
0xf3 | RETURN               terminate            0
0xf4 | DELEGATECALL         system               40
0xf5 | CREATE2              system               32000
0xfa | STATICCALL           system               40
0xfd | REVERT               terminate            0
0xff | SELFDESTRUCT         terminate            0

```

### Library

#### accessing the instruction registry

* `registry.INSTRUCTIONS` holds instruction templates. These are the initial set ob instructions available to the evm. Keep the templates static/unchanged.
* To create a new instruction from a template either use `instruction.clone()` or `registry.create_instruction(name=; or opcode=)`. Feel free to do anything you want with this new instance of an evm instruction. 
* To add new instructions just create an `Instruction(...)` object and put it into `registry.INSTRUCTIONS`


```python
from evm_instruction import registry

# access via named dict
jmp = registry.instruction.JUMP

# access via dict
## accessing the template objects (avoid modifying them)

jmp = registry.INSTRUCTIONS_BY_OPCODE["JUMP"]  # get the template object from the instruction registry 
jmp = registry.INSTRUCTIONS_BY_NAME["JUMP"]  # get the template object from the instruction registry 

jmp = jmp.clone()  # clone a new instruction from the template object

## creating new instruction objects from the template 
jmp = registry.create_instruction(name="JUMP")  # create a new jump instruction object in order to keep (

# access via categories lookup
terminating_instructions = registry.INSTRUCTIONS_BY_CATEGORY["terminate"]

# access all instructions as a list (no guarantee this is sorted in the future)
list_of_all_instructions = registry.INSTRUCTIONS

# extract certain instructions
list_of_gas_heavy_instructions = [i for i in registry.INSTRUCTIONS if i.gas > 500]

```

#### disassembling bytecode

* to work with evm-bytecode create a new `EvmBytecode(...)` object. It either takes `bytes`, `0x<hexstr>` or `hexstr`
* use `EvmBytecode.disassemble()` to transform it into a `EvmInstructions(...)` object (actually a custom `list` of `Instruction(...)` objects)
* use `EvmInstructions.assemble()` to transform it into a `EvmBytecode(...)` object. 
 
```python
# disassemble

evm_bytecode = '606060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806319e30bc7146100775780635bd74afe146101055780639df211541461017f578063b1d131bf146101ad575b6000366001919061007492919061042d565b50005b341561008257600080fd5b61008a610202565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156100ca5780820151818401526020810190506100af565b50505050905090810190601f1680156100f75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b61017d600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050919080359060200190919050506102a0565b005b6101ab600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190505061038d565b005b34156101b857600080fd5b6101c0610408565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b60018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102985780601f1061026d57610100808354040283529160200191610298565b820191906000526020600020905b81548152906001019060200180831161027b57829003601f168201915b505050505081565b3373ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415156102fb57600080fd5b8273ffffffffffffffffffffffffffffffffffffffff16818360405180828051906020019080838360005b83811015610341578082015181840152602081019050610326565b50505050905090810190601f16801561036e5780820380516001836020036101000a031916815260200191505b5091505060006040518083038185876187965a03f19250505050505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f19350505050151561040557600080fd5b50565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061046e57803560ff191683800117855561049c565b8280016001018555821561049c579182015b8281111561049b578235825591602001919060010190610480565b5b5090506104a991906104ad565b5090565b6104cf91905b808211156104cb5760008160009055506001016104b3565b5090565b905600a165627a7a723058202592c848fd2bdbf19b6558815a8c0a67519b4ad552eb001c92109a188ef215950029'
 
evmcode = EvmBytecode(evm_bytecode)  # can be hexstr, 0xhexstr or bytes
evminstructions = evmcode.disassemble()  #  returns an EvmInstructions object (actually a list of new instruction objects)
 
# print instructions
for instr in evminstructions:
    print(instr.name)
 
# assemble instructions
print(evm_bytecode == evminstructions.assemble().as_hexstring)  # assemble the instructionlist
 
```
