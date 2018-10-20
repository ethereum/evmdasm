#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>

import string
import binascii


def str_to_bytes(s):
    """
    Convert 0xHexString to bytes
    :param s: 0x hexstring
    :return:  byte sequence
    """
    try:
        return bytes.fromhex(s.replace("0x", ""))
    except (NameError, AttributeError):
        return s.decode("hex")


def bytes_to_str(s, prefix="0x"):
    return "%s%s" % (prefix,binascii.hexlify(s).decode("utf-8"))


def strip_0x_prefix(s):
    if not s.startswith("0x"):
        return s

    return s[2:]  # strip 0x


def is_hexstring(s):
    hex_digits = set(string.hexdigits)
    # if s is long, then it is faster to check against a set
    return all(c in hex_digits for c in s)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))