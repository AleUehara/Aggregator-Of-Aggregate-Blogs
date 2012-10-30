#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
import logging
import aggregator_env_variables
from blog import BlogInfo
from linklog.execute import Linklog
from atoananet.execute import AToaNaNet
from config_aggregator import Configuration
from datetime import date, timedelta, datetime

logging.basicConfig(filename=os.environ['AGGREGATOR_LOG'],level=logging.WARNING)
CONFIG = Configuration(os.environ['BLOG_CONFIG'])


def call_aggregator_login(blog):
	aggregators = [AToaNaNet(blog)]
	for aggregator in aggregators:
        aggregator.login()
		aggregator.sendpost()

def call_aggregator_without_login(blog):
	aggregators = [Linklog(blog)]
	for aggregator in aggregators:
		aggregator.sendpost()


def find_blogs():
	blogs = []
	for configblog in CONFIG.groups():
		blog = BlogInfo(configblog)
		blogs.append(blog)
	return blogs


def main():
	for blog in find_blogs():
		#call_aggregator_login(blog)
		call_aggregator_without_login(blog)

if __name__ == "__main__":
    try:
        logging.warning('------Inicio--- %s', datetime.today())
        main()
    except Exception, e:
        print e		
        logging.error('Erro main:', e)
    
    finally:
    	logging.warning('------Fim--- %s', datetime.today())