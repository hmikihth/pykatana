#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import re

class Decommentator():
  def __init__(self):
      pass
    
    
  def set_source(self, source):
      self.source = source
      self.source = self.del_oneliners()
      self.source = self.del_multiliners()

 
  def del_oneliners(self):
      result = re.sub(r'#.*[^\n]', '', self.source)
      if result:
        return result
      return None


  def del_multiliners(self):
      result = re.sub(r'(?<!([\=\[\(\{][\s*]))""".*\s*.*"""', '', self.source)
      if result:
        return result
      return None
      
  def get_source(self):
      return self.source
