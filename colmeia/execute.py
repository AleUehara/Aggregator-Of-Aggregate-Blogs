#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
import sys
import mechanize
import logging
from datetime import date, timedelta, datetime
from aggregator import AggregatorSiteLoginNotRequired

logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'log', 'linklog.log'),level=logging.WARNING)

class Colmeia(AggregatorSiteLoginNotRequired):
	def __init__(self, blog):
		AggregatorSiteLoginNotRequired.__init__(self, blog, 'colmeia')

	def sendpost(self):
		self.mech.open(self.url_sendpost)
		#for f in self.mech.forms():
		#	print f
		
		'''
		#Submit Image
		self.mech.select_form(nr=1)
		self.mech.form.add_file(open("/home/alexandre/scripts/aggregator/images/android.jpg"), 'text/plain', "android.jpg")
		response1 = self.mech.submit()

		image_response = self.mech.response().read()
		imagename = image_response.split("<div id=\"com_key\">")[1].split("</div>")[0]
		print imagename
		
		
		#Submit post
		self.mech.open(self.url_sendpost)
		self.mech.select_form(nr=0)
		self.mech.form['post_blog']      = [self.blog.colmeia]
		self.mech.form['post_link']      = ''
		self.mech.form['post_title']     = ''
		self.mech.form['post_cat']       = ['4'] #Curiosidade
		self.mech.form['post_desc']      = ''
		self.mech.form['post_tags']      = self.blog.tags

		#self.mech.form['post_blog']      = ["18820"]
		#self.mech.form['post_link']      = "http://cemporcentoandroid.blogspot.com/teste"
		#self.mech.form['post_title']     = "Novo Post do Blog"
		#self.mech.form['post_cat']       = ['4'] #Curiosidade
		#self.mech.form['post_desc']      = "Novo post do blog http://cemporcentoandroid.blogspot.com/ que fala sobre Android e outros dispositivos moveis, assim como celulares e sistemas operaconais"
		#self.mech.form['post_tags']      = "teste, android, celular, blog"

		#Realmente necessário???
		#<HiddenControl(post_img_key=) (readonly)>
		#<HiddenControl(post_email=) (readonly)>


		response1 = self.mech.submit()
		'''
		

		'''
		colmeia = open("testecolmeia.html", 'w')
		colmeia.write(self.mech.response().read())
		colmeia.close()
		'''
		