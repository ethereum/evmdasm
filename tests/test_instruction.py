#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>

import unittest

from evmdasm import registry, utils


class InstructionTest(unittest.TestCase):

    def test_instruction_attrib_protection(self):
        jmp = registry.instruction.JUMP

        # check protection of attributes of Instruction
        # make sure these attribs raise exceptions
        for attrib in ("opcode", "name", "length_of_operand", "description", "args", "returns", "gas", "category", "pops", "pushes"):
            with self.assertRaises(AttributeError) as context:
                setattr(jmp, attrib, 1)

        # check unprotected attribs
        for attrib in ("next", "previous", "address"):
            setattr(jmp, attrib, 1)


    def test_instruction_set_operand(self):
        value = "c0fefe"
        push = registry.create_instruction("PUSH%d"%len(value))
        push.operand = value

        self.assertEqual(push.operand, value)
        self.assertEqual(push.operand_bytes, utils.str_to_bytes(value))
        self.assertEqual(push.operand_length, len(value))

    def test_instruction_set_operand_bytes(self):
        value = b'\xc0\xfe\xfe'
        push = registry.create_instruction("PUSH%d" % len(value))
        push.operand_bytes = value

        self.assertEqual(push.operand, utils.bytes_to_str(value, prefix=""))
        self.assertEqual(push.operand_bytes, value)
        self.assertEqual(push.operand_length, len(value))


