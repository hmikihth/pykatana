#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Builder():
    def __init__(self):
        self.blocks = []
  
  
    def set_blocks(self, blocks):
        self.blocks = blocks
  
      
    def set_imported_objects(self, imported_objects):
        self.imported_objects = imported_objects      
  
  
    def mapping(self):
        for block in self.blocks:
            for obj in self.imported_objects:
                block.check_an_imported_object(obj)
                    
        for obj in self.imported_objects:
            if obj.parentname is not None:
                for obj2 in self.imported_objects:
                    if obj.parentname == obj2.name:
                        obj.add_related_object(obj2)
    