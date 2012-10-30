#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
import aggregator_env_variables
from config_aggregator import Configuration

CONFIG = Configuration(os.environ['BLOG_CONFIG'])

class BlogInfo():
	def __init__(self, configname):
		self.configname    = configname
		self.name  = CONFIG.read('name', self.configname)
		self.url   = CONFIG.read('url', self.configname)



if __name__ == "__main__":
    try:
    	bloginfo = BlogInfo('supermariodiscovery')
    	print bloginfo.name
        
    except Exception, e:
    	print e
