#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
import sys
import mechanize
import logging
from datetime import date, timedelta, datetime
from aggregator import AggregatorSiteLoginNotRequired

logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'log', 'linklog.log'),level=logging.WARNING)

class Linklog(AggregatorSiteLoginNotRequired):
	def __init__(self):
		AggregatorSiteLoginNotRequired.__init__(self, 'linklog')
		print 'ok'


#http://www.linklog.com.br/links/enviar		