#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>
import logging
from . import registry, utils

logger = logging.getLogger(__name__)


class EvmDisassembler(object):

    def __init__(self, debug=False, _registry=None):
        self.errors = []
        self.debug = debug
        self._registry = _registry if _registry is not None else registry.registry

    def disassemble(self, bytecode):
        """ Disassemble evm bytecode to a Instruction objects """

        pc = 0
        previous = None

        if not isinstance(bytecode, EvmBytecode):
            # normalize input
            evmbytecode = EvmBytecode(bytecode)

        iter_bytecode = iter(evmbytecode.as_bytes)

        # disassemble
        seen_stop = False
        for opcode in iter_bytecode:
            logger.debug(opcode)
            try:
                instruction = self._registry.by_opcode[opcode].consume(iter_bytecode)
                if not len(instruction.operand_bytes)==instruction.length_of_operand:
                    logger.error("invalid instruction: %s" % instruction.name)
                    instruction._name = "INVALID_%s" % hex(opcode)
                    instruction._description = "Invalid operand"
                    instruction._category = "unknown"

            except KeyError as ke:
                instruction = self._registry._template_cls(opcode=opcode,
                                          name="UNKNOWN_%s" % hex(opcode),
                                          description="Invalid opcode",
                                          category="unknown")

                if not seen_stop:
                    msg = "error: byte at address %d (%s) is not a valid operator" % (pc, hex(opcode))
                    if self.debug:
                        logger.exception(msg)
                    self.errors.append("%s; %r" % (msg, ke))
            if instruction.name == 'STOP' and not seen_stop:
                seen_stop = True

            instruction.address = pc
            pc += instruction.size
            # doubly link
            instruction.previous = previous
            if previous:
                previous.next = instruction

            # current is previous
            previous = instruction

            logger.debug("%s: %s %s" % (hex(instruction.address), instruction.name, instruction.operand))
            yield instruction

    def assemble(self, instructions):
        """ Assemble a list of Instruction() objects to evm bytecode"""
        for instruction in instructions:
            yield instruction.serialize()


class EvmBytecode(object):

    def __init__(self, bytecode):
        self.bytecode = EvmBytecode.normalize_bytecode(bytecode)
        self.errors = []

    def __str__(self):
        return "0x%s" % self.as_hexstring

    @staticmethod
    def normalize_bytecode(bytecode):
        # check if input is hexstr or bytestr and remove any prefixes. we're working on bytecode
        if isinstance(bytecode, bytes):
            return utils.bytes_to_str(bytecode, prefix='')
        elif isinstance(bytecode, str):
            bytecode = utils.strip_0x_prefix(bytecode.strip())
            if utils.is_hexstring(bytecode):
                return bytecode

        raise Exception("invalid input format. hexstring (0x<hexstr>) or bytes accepted. %r"%bytecode)

    def disassemble(self):
        disassembler = EvmDisassembler()
        self.instructions = EvmInstructions(list(disassembler.disassemble(self.as_bytes)))
        self.errors = disassembler.errors
        return self.instructions

    @property
    def as_hexstring(self):
        return self.bytecode

    @property
    def as_bytes(self):
        return utils.str_to_bytes(self.bytecode)


class EvmInstructions(list):

    def __init__(self, instructions):
        self.extend(instructions)
        self.errors = []

    def assemble(self):
        assembler = EvmDisassembler()
        self.bytecode = EvmBytecode(''.join(assembler.assemble(self)))
        self.errors = assembler.errors
        return self.bytecode

    def insert(self, index, obj):
        ret = super().insert(index, obj)
        self._fix_addresses()
        return ret

    def _fix_addresses(self):
        pc = 0
        for instr in self:
            instr.address = pc
            pc += len(instr)

    @property
    def as_string(self):
        return '\n'.join("%s %s" % (i.name, i.operand) for i in self)
