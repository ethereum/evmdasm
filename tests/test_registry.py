#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>

import unittest

from evmdasm import registry, instructions


class RegistryTest(unittest.TestCase):

    def test_access_by_attribute_and_dict(self):
        self.assertEqual(registry.instruction.JUMP, registry.INSTRUCTIONS_BY_NAME["JUMP"])

    def test_categories_set(self):
        for i in registry.INSTRUCTIONS:
            self.assertTrue(i.category)

    def test_create_instruction(self):
        self.assertEqual(registry.instruction.JUMP, registry.INSTRUCTIONS_BY_NAME["JUMP"])
        self.assertNotEqual(registry.instruction.JUMP, registry.create_instruction(name="JUMP"))

    def test_interface(self):
        for name in registry.INSTRUCTION_MARKS_BASICBLOCK_END:
            self.assertIsInstance(name, str)

        self.assertTrue(registry.INSTRUCTIONS)
        for instr in registry.INSTRUCTIONS:
            self.assertIsInstance(instr, instructions.Instruction)

        self.assertTrue(registry.INSTRUCTIONS_BY_OPCODE)
        for instr in registry.INSTRUCTIONS_BY_OPCODE.values():
            self.assertIsInstance(instr, instructions.Instruction)

        self.assertTrue(registry.INSTRUCTIONS_BY_NAME)
        for instr in registry.INSTRUCTIONS_BY_NAME.values():
            self.assertIsInstance(instr, instructions.Instruction)

        self.assertTrue(registry.INSTRUCTIONS_BY_CATEGORY)
        for instrs in registry.INSTRUCTIONS_BY_CATEGORY.values():
            for inst in instrs:
                self.assertIsInstance(instr, instructions.Instruction)

        # test one instruction
        self.assertIsInstance(registry.instruction.JUMP, instructions.Instruction)

        self.assertTrue(registry.INSTRUCTION_MARKS_BASICBLOCK_END)
        for name in registry.INSTRUCTION_MARKS_BASICBLOCK_END:
            self.assertIsInstance(name, str)


class MyInstruction(instructions.Instruction):

    def __init__(self, opcode, name, length_of_operand=0, description=None, args=None, returns=None, gas=-1,
                 category=None):
        super().__init__(opcode=opcode, name=name,
                         length_of_operand=length_of_operand,
                         description=description,
                         args=args, returns=returns,
                         gas=gas, category=category)

        # additional attribs
        self.annotations = []
        self.xrefs = set([])
        self.jumpto = None
        self.basicblock = None


class InstructionRegistryTest(unittest.TestCase):

    def setUp(self):
        self.registry = registry.InstructionRegistry(instructions=registry.INSTRUCTIONS, _template_cls=MyInstruction)

    def test_custom_template(self):
        self.assertTrue(self.registry.instructions)
        for instr in self.registry.instructions:
            self.assertIsInstance(instr, MyInstruction)
            self.assertTrue(hasattr(instr, "xrefs"))

        self.assertTrue(self.registry.by_opcode)
        for instr in self.registry.by_opcode.values():
            self.assertIsInstance(instr, MyInstruction)

        self.assertTrue(self.registry.by_name)
        for instr in self.registry.by_name.values():
            self.assertIsInstance(instr, MyInstruction)

        self.assertTrue(self.registry.by_category)
        for instrs in self.registry.by_category.values():
            for inst in instrs:
                self.assertIsInstance(instr, MyInstruction)

        # test one instruction
        self.assertIsInstance(self.registry.instruction.JUMP, MyInstruction)

        self.assertTrue(self.registry.instruction_marks_basicblock_end)
        for name in self.registry.instruction_marks_basicblock_end:
            self.assertIsInstance(name, str)


