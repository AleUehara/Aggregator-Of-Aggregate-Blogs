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
	def __init__(self, blog):
		AggregatorSiteLoginNotRequired.__init__(self, blog, 'linklog')

	def sendpost(self):
		self.mech.open(self.url_sendpost)
		'''
		self.mech.select_form(nr=1)
		self.mech.form['data[Link][li_blog]']     = self.blog.name
		self.mech.form['data[Link][li_bloglink]'] = self.blog.url
		self.mech.form['data[Link][categoria_id]']= ['2'] #Curiosidades
		self.mech.form['data[Link][li_titulo]']   = "Teste"
		self.mech.form['data[Link][li_link]']     = "http://www.globo.com/"
		self.mech.form.add_file(open("/home/alexandre/scripts/aggregator/images/sampleimgup.jpg"), 'text/plain', "sampleimgup.jpg")

		response1 = self.mech.submit()
		'''
		print self.blog.url
		print '------'

#http://www.linklog.com.br/links/enviar		