#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>


class BaseArgument(str): pass

    # todo: override ID to make it compare to the same


class Internal(BaseArgument):
    _type = "internal"


class Value(BaseArgument):
    _type = "int64"


class Address(BaseArgument):
    _type = "int160"


class Label(BaseArgument):
    _type = "label"


class Bool(BaseArgument):
    _type = "boolean"


class Byte(BaseArgument):
    _type = "byte"


class Word(BaseArgument):
    _type = "word"


class Index32(BaseArgument):
    _type = "index32"


class Index64(BaseArgument):
    _type = "index64"


class Index256(BaseArgument):
    _type = "index256"


class MemOffset(BaseArgument):
    _type = "memoffset"


class Length(BaseArgument):
    _type = "length"


class Gas(BaseArgument):
    _type = "gas"


class CallValue(BaseArgument):
    _type = "callvalue"


class Data(BaseArgument):
    _type = "data"


class Timestamp(BaseArgument):
    _type = "timestamp"
