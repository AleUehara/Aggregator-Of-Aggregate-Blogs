#!/usr/bin/python
# -*- encoding: utf-8 -*-

import ConfigParser

class Configuration(object):
  def __init__(self, config_file):
    self.config = ConfigParser.RawConfigParser()
    self.config.read(config_file)
  def read(self, name, group='directory'):
    return self.config.get(group, name) 
  def items(self, group='directory'): 
    return self.config.items(group)
  def groups(self):
  	return self.config.sections()
