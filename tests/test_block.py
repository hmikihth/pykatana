#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import unittest
from pykatana.block import Block
from pykatana.impob import ImpOb

class TestBlock(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

      
    def setUp(self):
        self.block = Block()     


    def test_set_source(self):
        source = "tryit"
        self.block.set_source(source)
        self.assertEqual(source, self.block.source)


    def test_find_type(self):
        types = {
            "function":"def something", 
            "class":"class something", 
            "logic":"if something"
        }
      
        for type in types:
            with self.subTest(type=type):
                 self.block.set_source(types[type])
                 self.block.find_type()
                 self.assertEqual(type, self.block.type, "The source type has to be %r." % type)

        
    def test_get_type(self):
        self.block.set_source("def something")
        self.assertEqual("function", self.block.get_type())


    def test_check_an_imported_object(self):
        objectname = "myobject"
        obj = ImpOb(objectname)

        tests = [
            ["def something():\n    " + objectname + "()", True],
            ["def something():\n    print  " + objectname + "()", True],
            ["def something():\n    something." + objectname + "()", False],
            ["def something():\n    something," + objectname + "()", True],
            ["class something(" + objectname + ")", True],
            ["class something(  " + objectname + "  )", True],
            ["class something" + objectname + "()", False],
            ["class something(" + objectname + ", other)", True],
            ["class something(other, " + objectname + ")", True]
        ]
        
        for test in tests:
            with self.subTest(test=test):
                self.block.set_source(test[0])
                result = self.block.check_an_imported_object(obj)
                if test[1]:
                    self.assertTrue(result)      
                else:
                    self.assertFalse(result)      


    def test_get_blockname(self):
        blocks = {
            "name1":"def name1(): pass",
            "name2":"class name2 (uff): pass",
            "name3":"@dec\nclass name3 (uff): pass"
        }
      
        for name in blocks:
            with self.subTest(name=name):
                self.block.set_source(blocks[name])
                result = self.block.get_blockname()
                self.assertEqual(name, result)

        self.block.set_source("if something")
        result = self.block.get_blockname()
        self.assertIsNone(result)

    def test_get_related_imports(self):
        source = "def something():\n    relfv1(); relfv2()"
        objects = ["relfv1", "relfv2", "falsefv"]
        objects = list(map(lambda e: ImpOb(e), objects))
        self.block.set_source(source)
        for obj in objects:
            self.block.check_an_imported_object(obj)
        result = self.block.get_related_imports()
        for obj in objects:
            with self.subTest(obj=obj):
                if obj.name != "falsefv":
                    self.assertIn(obj, result)
                else:
                    self.assertNotIn(obj, result)
