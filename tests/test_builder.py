#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import unittest

from pykatana.block import Block
from pykatana.impob import ImpOb

from pykatana.builder import Builder

class TestBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = Builder()
  
    def test_set_blocks(self):
        blocks = [Block("def stg():\n    pass")]
        self.builder.set_blocks(blocks)
        self.assertEqual(blocks, self.builder.blocks)
      
      
    def test_set_imported_objects(self):
        imported_objects = [ImpOb("stg")]
        self.builder.set_imported_objects(imported_objects)
        self.assertIs(imported_objects[0], self.builder.imported_objects[0])


    def test_mapping(self):
        blocks = [Block("def myfunc():\n    stg()")]
        imported_objects = [ImpOb("stg")]
        self.builder.set_blocks(blocks)
        self.builder.set_imported_objects(imported_objects)
        self.builder.mapping()
        self.assertIn(imported_objects[0], blocks[0].related_imports)
      
      
    def get_groups(self):
        pass
