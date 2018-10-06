#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>
import logging
import itertools
from . import utils

logger = logging.getLogger(__name__)


class Instruction(object):
    """ Base Instruction class

        doubly linked
    """

    def __init__(self, opcode, name, length_of_operand=0, description=None, args=None, returns=None, gas=-1, category=None):
        # static
        self.opcode, self.name, self.length_of_operand = opcode, name, length_of_operand
        self.gas = gas
        self.description = description
        self.args = args or []  # number of arguments the instruction takes from stack
        self.returns = returns or []  # number of results returned (0 or 1)
        self.category = category  # instruction category

        # dynamic
        self.opcode_bytes = (self.opcode).to_bytes(1, byteorder="big")
        self.operand_bytes = b'\x00'*length_of_operand  # sane default
        self.operand = '\x00'*length_of_operand  # sane default
        self.address = None
        self.next = None
        self.previous = None

    def clone(self):
        return Instruction(opcode=self.opcode,
                           name=self.name,
                           length_of_operand=self.length_of_operand,
                           description=self.description,
                           args=self.args, returns=self.returns,
                           gas=self.gas,
                           category=self.category)

    def __repr__(self):
        return "<%s name=%s address=%s size=%d %s>" % (self.__class__.__name__,
                                                       self.name, hex(self.address), self.size(),
                                                       "operand=%r" % self.operand if self.operand else "")

    def __str__(self):
        return "%s %s" % (self.name, "0x%s" % self.operand if self.operand else '')

    def size(self):
        return self.length_of_operand + 1  # opcode + operand

    def consume(self, bytecode):
        # clone
        m = self.clone()
        # consume
        m.set_operand(bytes(_ for _ in itertools.islice(bytecode, m.length_of_operand)))
        return m

    def set_operand(self, b):
        self.operand_bytes = b
        self.operand = ''.join('%0.2x' % _ for _ in self.operand_bytes)
        return self

    def serialize(self):
        return ("%0.2x" % self.opcode)+utils.bytes_to_str(self.operand_bytes, prefix="")

    def skip_to(self, names):
        res = self.next
        while res:
            if any(res.name==name for name in names):
                return res
            res = res.next
        return None
