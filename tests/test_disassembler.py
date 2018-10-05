#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>

import unittest

from evm_instruction import EvmDisassembler, EvmBytecode, EvmInstructions, Instruction
import evm_instruction.utils as utils


class EvmBytecodeTest(unittest.TestCase):

    def setUp(self):
        self.testcode = '606060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806319e30bc7146100775780635bd74afe146101055780639df211541461017f578063b1d131bf146101ad575b6000366001919061007492919061042d565b50005b341561008257600080fd5b61008a610202565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156100ca5780820151818401526020810190506100af565b50505050905090810190601f1680156100f75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b61017d600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050919080359060200190919050506102a0565b005b6101ab600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190505061038d565b005b34156101b857600080fd5b6101c0610408565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b60018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102985780601f1061026d57610100808354040283529160200191610298565b820191906000526020600020905b81548152906001019060200180831161027b57829003601f168201915b505050505081565b3373ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415156102fb57600080fd5b8273ffffffffffffffffffffffffffffffffffffffff16818360405180828051906020019080838360005b83811015610341578082015181840152602081019050610326565b50505050905090810190601f16801561036e5780820380516001836020036101000a031916815260200191505b5091505060006040518083038185876187965a03f19250505050505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f19350505050151561040557600080fd5b50565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061046e57803560ff191683800117855561049c565b8280016001018555821561049c579182015b8281111561049b578235825591602001919060010190610480565b5b5090506104a991906104ad565b5090565b6104cf91905b808211156104cb5760008160009055506001016104b3565b5090565b905600a165627a7a723058202592c848fd2bdbf19b6558815a8c0a67519b4ad552eb001c92109a188ef215950029'
        #print(utils.str_to_bytes(self.testcode))
        self.testcode_bytes = b'```@R`\x046\x10a\x00bW`\x005|\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x04c\xff\xff\xff\xff\x16\x80c\x19\xe3\x0b\xc7\x14a\x00wW\x80c[\xd7J\xfe\x14a\x01\x05W\x80c\x9d\xf2\x11T\x14a\x01\x7fW\x80c\xb1\xd11\xbf\x14a\x01\xadW[`\x006`\x01\x91\x90a\x00t\x92\x91\x90a\x04-V[P\x00[4\x15a\x00\x82W`\x00\x80\xfd[a\x00\x8aa\x02\x02V[`@Q\x80\x80` \x01\x82\x81\x03\x82R\x83\x81\x81Q\x81R` \x01\x91P\x80Q\x90` \x01\x90\x80\x83\x83`\x00[\x83\x81\x10\x15a\x00\xcaW\x80\x82\x01Q\x81\x84\x01R` \x81\x01\x90Pa\x00\xafV[PPPP\x90P\x90\x81\x01\x90`\x1f\x16\x80\x15a\x00\xf7W\x80\x82\x03\x80Q`\x01\x83` \x03a\x01\x00\n\x03\x19\x16\x81R` \x01\x91P[P\x92PPP`@Q\x80\x91\x03\x90\xf3[a\x01}`\x04\x80\x805s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16\x90` \x01\x90\x91\x90\x805\x90` \x01\x90\x82\x01\x805\x90` \x01\x90\x80\x80`\x1f\x01` \x80\x91\x04\x02` \x01`@Q\x90\x81\x01`@R\x80\x93\x92\x91\x90\x81\x81R` \x01\x83\x83\x80\x82\x847\x82\x01\x91PPPPPP\x91\x90\x805\x90` \x01\x90\x91\x90PPa\x02\xa0V[\x00[a\x01\xab`\x04\x80\x805s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16\x90` \x01\x90\x91\x90PPa\x03\x8dV[\x00[4\x15a\x01\xb8W`\x00\x80\xfd[a\x01\xc0a\x04\x08V[`@Q\x80\x82s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16\x81R` \x01\x91PP`@Q\x80\x91\x03\x90\xf3[`\x01\x80T`\x01\x81`\x01\x16\x15a\x01\x00\x02\x03\x16`\x02\x90\x04\x80`\x1f\x01` \x80\x91\x04\x02` \x01`@Q\x90\x81\x01`@R\x80\x92\x91\x90\x81\x81R` \x01\x82\x80T`\x01\x81`\x01\x16\x15a\x01\x00\x02\x03\x16`\x02\x90\x04\x80\x15a\x02\x98W\x80`\x1f\x10a\x02mWa\x01\x00\x80\x83T\x04\x02\x83R\x91` \x01\x91a\x02\x98V[\x82\x01\x91\x90`\x00R` `\x00 \x90[\x81T\x81R\x90`\x01\x01\x90` \x01\x80\x83\x11a\x02{W\x82\x90\x03`\x1f\x16\x82\x01\x91[PPPPP\x81V[3s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16`\x00\x80\x90T\x90a\x01\x00\n\x90\x04s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16\x14\x15\x15a\x02\xfbW`\x00\x80\xfd[\x82s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16\x81\x83`@Q\x80\x82\x80Q\x90` \x01\x90\x80\x83\x83`\x00[\x83\x81\x10\x15a\x03AW\x80\x82\x01Q\x81\x84\x01R` \x81\x01\x90Pa\x03&V[PPPP\x90P\x90\x81\x01\x90`\x1f\x16\x80\x15a\x03nW\x80\x82\x03\x80Q`\x01\x83` \x03a\x01\x00\n\x03\x19\x16\x81R` \x01\x91P[P\x91PP`\x00`@Q\x80\x83\x03\x81\x85\x87a\x87\x96Z\x03\xf1\x92PPPPPPPV[`\x00\x80\x90T\x90a\x01\x00\n\x90\x04s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16a\x08\xfc0s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x161\x90\x81\x15\x02\x90`@Q`\x00`@Q\x80\x83\x03\x81\x85\x88\x88\xf1\x93PPPP\x15\x15a\x04\x05W`\x00\x80\xfd[PV[`\x00\x80\x90T\x90a\x01\x00\n\x90\x04s\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x16\x81V[\x82\x80T`\x01\x81`\x01\x16\x15a\x01\x00\x02\x03\x16`\x02\x90\x04\x90`\x00R` `\x00 \x90`\x1f\x01` \x90\x04\x81\x01\x92\x82`\x1f\x10a\x04nW\x805`\xff\x19\x16\x83\x80\x01\x17\x85Ua\x04\x9cV[\x82\x80\x01`\x01\x01\x85U\x82\x15a\x04\x9cW\x91\x82\x01[\x82\x81\x11\x15a\x04\x9bW\x825\x82U\x91` \x01\x91\x90`\x01\x01\x90a\x04\x80V[[P\x90Pa\x04\xa9\x91\x90a\x04\xadV[P\x90V[a\x04\xcf\x91\x90[\x80\x82\x11\x15a\x04\xcbW`\x00\x81`\x00\x90UP`\x01\x01a\x04\xb3V[P\x90V[\x90V\x00\xa1ebzzr0X %\x92\xc8H\xfd+\xdb\xf1\x9beX\x81Z\x8c\ngQ\x9bJ\xd5R\xeb\x00\x1c\x92\x10\x9a\x18\x8e\xf2\x15\x95\x00)'

    def test_disassembler_noerror(self):
        evmcode = EvmBytecode(self.testcode)
        self.assertFalse(evmcode.disassemble().errors)
        self.assertFalse(evmcode.disassemble().assemble().errors)

    def test_disassembler_0xhexstr(self):
        evmcode = EvmBytecode("0x%s" % self.testcode)
        self.assertEqual(evmcode.bytecode, self.testcode)
        self.assertIsInstance(evmcode.disassemble(), EvmInstructions)
        self.assertIsInstance(evmcode.disassemble().assemble(), EvmBytecode)
        self.assertEqual(utils.strip_0x_prefix(self.testcode), evmcode.disassemble().assemble().as_hexstring)

    def test_disassembler_hexstr(self):
        evmcode = EvmBytecode(self.testcode)
        self.assertEqual(evmcode.bytecode, self.testcode)
        self.assertIsInstance(evmcode.disassemble(), EvmInstructions)
        self.assertIsInstance(evmcode.disassemble().assemble(), EvmBytecode)
        self.assertEqual(self.testcode, evmcode.disassemble().assemble().as_hexstring)

    def test_disassembler_bytes(self):
        evmcode = EvmBytecode(self.testcode_bytes)
        self.assertEqual(self.testcode, evmcode.bytecode)
        self.assertIsInstance(evmcode.disassemble(), EvmInstructions)
        self.assertIsInstance(evmcode.disassemble().assemble(), EvmBytecode)
        self.assertEqual(self.testcode, evmcode.disassemble().assemble().as_hexstring)

    def test_instructions_string(self):
        evmcode = EvmBytecode(self.testcode_bytes)
        evmcode_listing = evmcode.disassemble().as_string
        self.assertIn("PUSH1 60\n", evmcode_listing)
        self.assertIn("\nUNKNOWN_0x29", evmcode_listing)


class EvmDisassemblerTest(unittest.TestCase):

    def setUp(self):
        self.testcode = '606060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806319e30bc7146100775780635bd74afe146101055780639df211541461017f578063b1d131bf146101ad575b6000366001919061007492919061042d565b50005b341561008257600080fd5b61008a610202565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156100ca5780820151818401526020810190506100af565b50505050905090810190601f1680156100f75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b61017d600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050919080359060200190919050506102a0565b005b6101ab600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190505061038d565b005b34156101b857600080fd5b6101c0610408565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b60018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102985780601f1061026d57610100808354040283529160200191610298565b820191906000526020600020905b81548152906001019060200180831161027b57829003601f168201915b505050505081565b3373ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415156102fb57600080fd5b8273ffffffffffffffffffffffffffffffffffffffff16818360405180828051906020019080838360005b83811015610341578082015181840152602081019050610326565b50505050905090810190601f16801561036e5780820380516001836020036101000a031916815260200191505b5091505060006040518083038185876187965a03f19250505050505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f19350505050151561040557600080fd5b50565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061046e57803560ff191683800117855561049c565b8280016001018555821561049c579182015b8281111561049b578235825591602001919060010190610480565b5b5090506104a991906104ad565b5090565b6104cf91905b808211156104cb5760008160009055506001016104b3565b5090565b905600a165627a7a723058202592c848fd2bdbf19b6558815a8c0a67519b4ad552eb001c92109a188ef215950029'

    def test_disassembler(self):
        disassembler = EvmDisassembler()
        instruction_list = list(disassembler.disassemble(self.testcode))
        self.assertTrue(instruction_list)
        self.assertIsInstance(instruction_list[0], Instruction)
        self.assertIsInstance(instruction_list[-1], Instruction)
        self.assertEqual(instruction_list[0].name, "PUSH1")

        self.assertEqual(''.join(disassembler.assemble(instruction_list)), self.testcode)

    def test_disassembler_0xinput(self):
        disassembler = EvmDisassembler()
        instruction_list = list(disassembler.disassemble("0x"+self.testcode))
        self.assertTrue(instruction_list)
        self.assertIsInstance(instruction_list[0], Instruction)
        self.assertIsInstance(instruction_list[-1], Instruction)
        self.assertEqual(instruction_list[0].name, "PUSH1")

        self.assertEqual(''.join(disassembler.assemble(instruction_list)), self.testcode)

