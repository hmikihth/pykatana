#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import unittest
import re

from pykatana.collector import Collector
from pykatana.impob import ImpOb
from pykatana.block import Block

class TestCollector(unittest.TestCase):
  @classmethod
  def setUpClass(self):
      pass

      
  def setUp(self):
      self.collector = Collector()

      
  def test_set_source(self):
      source = "def something():\n    pass\n"
      self.collector.set_source(source)
      self.assertEqual(source, self.collector.source)


  def test_find_imported_objects(self):
      sources = {
       "import zoo\ndef something():\n    pass\n":["zoo"],
       "import zoo\nimport aquarium\ndef something():\n    pass\n":["zoo","aquarium"],
       "from zoo import gorilla\ndef something():\n    pass\n":["gorilla"],
       "from zoo import camel, zebra\ndef something():\n    pass\n":["camel", "zebra"],
       "import zoo, aquarium, safari\ndef something():\n    pass\n":["zoo","aquarium","safari"],
       "import zoo as z\ndef something():\n    pass\n":["z"],
       "from zoo import lion as cat\ndef something():\n    pass\n":["cat"],
       "import zoo as z, aquarium as a\ndef something():\n    pass\n":["z"],
       "from zoo import lion as cat, wolf as dog\ndef something():\n    pass\n":["cat","dog"],
       "def something():\n    pass\n":[],
      }
      for source in sources:
          with self.subTest(source=source):
              self.collector.set_source(source)
              imported_objects = list(map(lambda e: e.name, self.collector.find_imported_objects()))
              for object in sources[source]:
                  with self.subTest(object=object):
                      self.assertIn(object, imported_objects)

      
  def test_get_imported_objects(self):
      source = "import zoo\ndef something():\n    pass\n"
      self.collector.set_source(source)
      result = self.collector.get_imported_objects()
      self.assertIs(type(result), list)
      self.assertEqual(len(result), 1)
      self.assertIs(type(result[0]), ImpOb)
      self.assertEqual(result[0].name, "zoo")

  def test_object_hunter(self):
      lines = [
       "from zoo import lion as cat",
       "import safari",
      ]
      result = self.collector.object_hunter(lines)
      self.assertEqual(result[0].name, "cat")
      self.assertEqual(result[1].name, "safari")
      self.assertEqual(result[0].parentname, "zoo")

      
  def test_find_blocks(self):
      sources = {
        "import zoo\ndef something():\n    pass\n":[["def something():\n    pass\n\n"], ""],
        "def something():\n    pass":[["def something():\n    pass\n"], ""],
        "def something():\n    pass\nmyvar=1\nclass Stg():\n    pass":[["def something():\n    pass\n", "class Stg():\n    pass\n"], "myvar=1\n"],
        "def something():\n    pass\n@mydec\n\n\nclass Stg():\n    pass":[["def something():\n    pass\n","@mydec\n\n\nclass Stg():\n    pass\n"],""],
        "if x:\n  pass\nelif x:\n  pass\nelse:\n  pass\ndef func():\n    pass\n":[["def func():\n    pass\n\n","if x:\n  pass\nelif x:\n  pass\nelse:\n  pass\n"],""],
        "try:\n    pass\nexcept:\n    pass\n":[["try:\n    pass\nexcept:\n    pass\n\n"],""],
        "while True:\n    pass\n":[["while True:\n    pass\n\n"],""],
        "for n in x:\n    pass\n":[["for n in x:\n    pass\n\n"],""],
      }
      for source in sources:
          with self.subTest(source=source):
              self.collector.set_source(source)
              blocks, others = self.collector.find_blocks()
              for block in sources[source][0]:
                  with self.subTest(block=block):
                      self.assertIn(block, blocks)
              self.assertEqual(sources[source][1], others)

      
  def test_get_blocks(self):
      source = "def something():\n    pass\n"
      self.collector.set_source(source)      
      result = self.collector.get_blocks()
      self.assertIs(type(result[0]), Block)
      self.assertEqual(result[0].source, source+'\n')


  def test_get_others(self):
      source = "vari=7"
      self.collector.set_source(source)      
      result = self.collector.get_others()
      self.assertEqual(result, source+'\n')
