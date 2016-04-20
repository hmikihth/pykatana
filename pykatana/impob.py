#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class ImpOb():
    def __init__(self, name):
        self.set_name(name)
        self.parentname = None
        self.parent_impob = None
        self.parentname = None


    def set_name(self, name):
        self.name = name


    def set_source(self, source):
        self.source = source
      
      
    def set_parentname(self, parentname):
        self.parentname = parentname
       
  
    def set_parentname(self, parentname):
        self.parentname = parentname  
      
      
    def find_parent(self, objects):
       if self.parentname is not None:
           for obj in objects:
               if obj.name == self.parentname:
                   self.add_related_object(obj)
               