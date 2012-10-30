#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
import sys
import mechanize
import logging
from datetime import date, timedelta, datetime
from aggregator import AggregatorSiteLoginRequired

logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'log', 'linklog.log'),level=logging.WARNING)

class AToaNaNet(AggregatorSiteLoginRequired):
	def __init__(self):
		AggregatorSiteLoginRequired.__init__(self, 'atoananet')
		self.mech.addheaders.append(
			("Cookie","__utma=142820197.825007049.1351515992.1351515992.1351515992.1; __utmc=142820197; __utmz=142820197.1351515992.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); PHPSESSID=cfa7c7df2b2d47641a2b6b04e9e17716")
			)