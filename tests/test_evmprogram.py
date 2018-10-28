#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>

import unittest
import random

from evmdasm import EvmInstructions, EvmProgram, registry, Instruction



class EvmInstructionTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_assemble(self):
        p = EvmProgram()
        p.push(1)
        p.push(0x0101)
        p.op("JUMPDEST")
        p.push(0xc0fefe)

        assembled = p.assemble()

        self.assertEqual(assembled.as_hexstring, "60016101015b62c0fefe")

        expect = [("PUSH1","01"),
                  ("PUSH2","0101"),
                  ("JUMPDEST",""),
                  ("PUSH3","c0fefe")]

        for idx,instr in enumerate(p.assemble().disassemble()):
            self.assertEqual(instr.name, expect[idx][0])
            self.assertEqual(instr.operand, expect[idx][1])

    def test_assemble_call_args(self):
        p = EvmProgram()
        p.push(1)
        p.push(0x0101)
        p.op("JUMPDEST")
        p.push(0xc0fefe)
        #T.Gas("gas"), T.Address("address"), T.CallValue("value"), T.MemOffset("inOffset"), T.Length("inSize"), T.MemOffset("retOffset"), T.Length("retSize")
        p.call(1,2,3,4,5,6,7)

        assembled = p.assemble()
        self.assertEqual(assembled.as_hexstring, "60016101015b62c0fefe6007600660056004600360026001f1")

        self.assertEqual(assembled.disassemble().as_string.strip(), """PUSH1 01
PUSH2 0101
JUMPDEST 
PUSH3 c0fefe
PUSH1 07
PUSH1 06
PUSH1 05
PUSH1 04
PUSH1 03
PUSH1 02
PUSH1 01
CALL""".strip())

    def test_assemble_call_kargs(self):
        p = EvmProgram()
        p.push(1)
        p.push(0x0101)
        p.op("JUMPDEST")
        p.push(0xc0fefe)
        # T.Gas("gas"), T.Address("address"), T.CallValue("value"), T.MemOffset("inOffset"), T.Length("inSize"), T.MemOffset("retOffset"), T.Length("retSize")
        p.call(gas=1, address=2, value=3, inOffset=4, inSize=5, retOffset=6, retSize=7)

        assembled = p.assemble()
        self.assertEqual(assembled.as_hexstring, "60016101015b62c0fefe6007600660056004600360026001f1")

        self.assertEqual(assembled.disassemble().as_string.strip(), """PUSH1 01
PUSH2 0101
JUMPDEST 
PUSH3 c0fefe
PUSH1 07
PUSH1 06
PUSH1 05
PUSH1 04
PUSH1 03
PUSH1 02
PUSH1 01
CALL""".strip())

    def test_assemble_call_kwargs_unsort(self):
        p = EvmProgram()
        p.push(1)
        p.push(0x0101)
        p.op("JUMPDEST")
        p.push(0xc0fefe)
        # T.Gas("gas"), T.Address("address"), T.CallValue("value"), T.MemOffset("inOffset"), T.Length("inSize"), T.MemOffset("retOffset"), T.Length("retSize")
        p.call(value=3, inOffset=4, inSize=5, retOffset=6,gas=1, address=2,  retSize=7)

        assembled = p.assemble()
        self.assertEqual(assembled.as_hexstring, "60016101015b62c0fefe6007600660056004600360026001f1")

        self.assertEqual(assembled.disassemble().as_string.strip(), """PUSH1 01
PUSH2 0101
JUMPDEST 
PUSH3 c0fefe
PUSH1 07
PUSH1 06
PUSH1 05
PUSH1 04
PUSH1 03
PUSH1 02
PUSH1 01
CALL""".strip())

    def test_instr_args_kwargs(self):
        p1 = EvmProgram()
        # T.Gas("gas"), T.Address("address"), T.CallValue("value"), T.MemOffset("inOffset"), T.Length("inSize"), T.MemOffset("retOffset"), T.Length("retSize")
        p1.call(value=3, inOffset=4, inSize=5, retOffset=6, gas=1, address=2, retSize=7)

        p2 = EvmProgram()
        #T.Gas("gas"), T.Address("address"), T.CallValue("value"), T.MemOffset("inOffset"), T.Length("inSize"), T.MemOffset("retOffset"), T.Length("retSize")
        p2.call(1,2,3,4,5,6,7)

        self.assertEqual(p1.assemble().as_hexstring,p2.assemble().as_hexstring)
