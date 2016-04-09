#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import unittest
from pykatana.decommentator import Decommentator

class TestDecommentator(unittest.TestCase):
  def test_set_source(self):
      source = "def fv():pass"
      dc = Decommentator()
      dc.set_source(source)
      self.assertEqual(source, dc.source)

  
  def test_del_oneliners(self):
      source = "def fv(x):#comment1\n#    print x\n    return x"
      commentless = "def fv(x):\n\n    return x"
      dc = Decommentator()
      dc.set_source(source)
      result = dc.del_oneliners()
      self.assertEqual(result, commentless)
      
      
  def test_del_multiliners(self):
      source = 'def fv(x):"""comment1\n    print x"""\n    return x\n"""monkey"""'
      commentless = "def fv(x):\n    return x\n"
      dc = Decommentator()
      dc.set_source(source)
      result = dc.del_multiliners()
      self.assertEqual(result, commentless)
      
      
  def test_get_source(self):
      source = 'def fv(x):"""comment1\n    print x"""\n    return x\n"""monkey"""\n# bonobo'
      commentless = "def fv(x):\n    return x\n\n"
      dc = Decommentator()
      dc.set_source(source)
      result = dc.get_source()
      self.assertEqual(result, commentless)
  
      source = 'def fv(x):\n    s= """x"""'
      dc = Decommentator()
      dc.set_source(source)
      result = dc.get_source()
      self.assertEqual(result, source)
  
#      source = 'mydict = {"something": """it will be \n    wrong"""}'
#      dc = Decommentator()
#      dc.set_source(source)
#      result = dc.get_source()
#      self.assertEqual(result, source)
           