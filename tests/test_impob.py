#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import unittest

from pykatana.impob import ImpOb

class TestImpOb(unittest.TestCase):
    def setUp(self):
        self.obj = ImpOb("myOb")

    def test_set_name(self):
        name = "myname"
        self.obj.set_name(name)
        self.assertEqual(name, self.obj.name)


    def test_set_source(self):
        source = "mysource"
        self.obj.set_source(source)
        self.assertEqual(source, self.obj.source)
      
      
    def test_set_parentname(self):
        parentname = "parent"
        self.obj.set_parentname(parentname)
        self.assertEqual(self.obj.parentname, parentname)
