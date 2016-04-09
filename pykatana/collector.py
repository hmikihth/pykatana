#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import re

from pykatana.impob import ImpOb
from pykatana.block import Block


class Collector():
  def __init__(self):
      pass
      

  def object_hunter(self, lines):
      result = []
      for line in lines:
        parent = re.match("(?:from\s+)(\w+)(?:\s+.*)", line)
        if parent is not None:
          parent = parent.group(1)
        line2 = re.match("(?:.*import\s+)(.*)", line).group(1)
        for e in line2.split(','):
          splitted = e.strip().split()
          if len(splitted) > 1:
            obj = ImpOb(splitted[2])
          else:
            obj = ImpOb(splitted[0])
          obj.set_source(line)
          if parent is not None:
            obj.set_parentname(parent)
          result.append(obj)
      for obj in result:
          obj.find_parent(result)
      return result

      
  def set_source(self, source):
      self.source = source
      self.imported_objects = self.find_imported_objects()
      blocks, self.others = self.find_blocks()
      self.blocks = list(map(lambda e: Block(e), blocks))

  
  def find_imported_objects(self):
      imported_objects = []
      pattern = r"((?:from\s*\w+\s*)?import\s\w+(?:\s+as\s+\w+)?(?:\s*,\s*\w+\s*(?:as\s+\w+)*)*)"
      p = re.compile(pattern)
      imported_objects = self.object_hunter( p.findall(self.source) )
      return imported_objects

      
  def get_imported_objects(self):
      return self.imported_objects

 
  def find_blocks(self):
      blocks = []
      others = ""
      block_source = ""
      inblock = False
      toothers = False
      for line in self.source.split("\n"):
          if line[:7] != "import " and line[:5] != "from ":
            if len(line) != 0 and line[0] == "@":
              if inblock:
                 blocks.append(block_source)
                 block_source = ""
                 inblock = False
            elif line[:6] in ["class ", "while "] or line[:5] == "with " or line[:4] in ["def ", "try:", "for "] or line[:3] == "if ":
              if inblock:
                 blocks.append(block_source)
                 block_source = ""
              inblock = True
            elif line[:5] in ["elif ", "else:"] or line[:6] == "except":
              pass
            elif len(line) != 0 and not line[0].isspace():
              toothers = True
            if toothers:
              others += line + '\n'
              toothers = False
            else:
              block_source += line + '\n'
      blocks.append(block_source)
      return blocks, others


  def get_blocks(self):
      return self.blocks


  def get_others(self):
      return self.others
