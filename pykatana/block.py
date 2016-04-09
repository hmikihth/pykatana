#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import re

class Block():
  def __init__(self, source=None):
      self.type = None
      if source is not None:
        self.set_source(source)
  
    
  def set_source(self, source):
      self.related_imports = []
      self.source = source  
      self.find_type()
      self.find_blockname()

    
  def find_type(self):
      pos = self.source.find("def ")
      if pos != -1:
        self.type = "function"
      else:
        pos = self.source.find("class ")
        if pos != -1:
          self.type = "class"
        else:
          self.type = "logic"
  
            
  def get_type(self):
      return self.type


  def check_an_imported_object(self, obj):
      i = 0
      for line in self.source.split('\n'):
          pattern = r'.*""".*' + obj.name + r'.*"""'
          p = re.compile(pattern)
          result = p.match(line)
          if result != None:
            return False
          if (i == 0) and (self.type == "class"):
            pattern = r'.*\((.*,\s*|\s*)' + obj.name + r'\s*.*'
          else:
            pattern = r'.*(\s|,)' + obj.name 
          p = re.compile(pattern)
          result = p.match(line)
          if result != None:
            self.related_imports.append(obj)
            return True
          i += 1
      return False


  def find_blockname(self):
      pattern = r'(?:.*\s*)(def|class)\s*(?P<name>\w+)(\s*|\().*'
      p = re.compile(pattern)
      result = p.match(self.source)
      try:
          self.blockname = result.group("name")
      except:
          self.blockname = None
    
      
  def get_blockname(self):
      return self.blockname


  def get_related_imports(self):
      return self.related_imports