#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>

import unittest

from evm_instruction import registry


class RegistryTest(unittest.TestCase):

    def test_access_by_attribute_and_dict(self):
        self.assertEqual(registry.instruction.JUMP, registry.INSTRUCTIONS_BY_NAME["JUMP"])

    def test_categories_set(self):
        for i in registry.INSTRUCTIONS:
            self.assertTrue(i.category)
