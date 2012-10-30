#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
import mechanize
import cookielib
import logging
import aggregator_env_variables
from config_aggregator import Configuration
from datetime import date, timedelta, datetime

CONFIG = Configuration(os.environ['AGGREGATOR_CONFIG'])
logging.basicConfig(filename=os.environ['AGGREGATOR_LOG'],level=logging.WARNING)

class Site(object):
	def __init__(self):
		self.mech          = mechanize.Browser()
		self.mech.set_handle_robots(False)

		self.cj = cookielib.LWPCookieJar()
		self.mech.set_cookiejar(self.cj)

		# Browser options
		self.mech.set_handle_equiv(True)
		#br.set_handle_gzip(True)
		self.mech.set_handle_redirect(True)
		self.mech.set_handle_referer(True)
		self.mech.set_handle_robots(False)

		# Follows refresh 0 but not hangs on refresh > 0
		#self.mech.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

		# Want debugging messages?
		#self.mech.set_debug_http(True)
		#self.mech.set_debug_redirects(True)
		#self.mech.set_debug_responses(True)

		# User-Agent (this is cheating, ok?)
		self.mech.addheaders = [
		("Connection", "keep-alive"),
		('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'),
		("Referer", "http://www.atoananet.com.br/usuarios/")
		]

class AggregatorSite(Site):
	def __init__(self, configname):
		Site.__init__(self)
		self.configname    = configname
		self.url_sendpost  = CONFIG.read('url_sendpost', self.configname)

	def sendpost(self):
		self.mech.open(self.url_sendpost)
		for f in self.mech.forms():
			print f		

class AggregatorSiteLoginRequired(AggregatorSite):
	def __init__(self, configname):
		AggregatorSite.__init__(self, configname)
		self.configname    = configname
		self.login_url     = CONFIG.read('login_url', self.configname)
		self.user          = CONFIG.read('user', self.configname)
		self.password      = CONFIG.read('password', self.configname)
		self.userform      = CONFIG.read('userform', self.configname)
		self.passwordform  = CONFIG.read('passwordform', self.configname)
		self.url_sendpost  = CONFIG.read('url_sendpost', self.configname)

	def login(self, formnumber=0):
		self.mech.open(self.login_url)
		self.mech.select_form(nr=formnumber)

		self.mech[self.userform] = self.user
		self.mech[self.passwordform] = self.password
		self.mech.submit()		

		self.mech.open(self.url_sendpost)

		print self.mech.geturl()


class AggregatorSiteLoginNotRequired(AggregatorSite):
	def __init__(self, configname):
		AggregatorSite.__init__(self, configname)



if __name__ == "__main__":
    try:
        logging.warning('------Inicio--- %s', datetime.today())

        aggregator = AggregatorSiteLoginRequired('teste')
        aggregator.login()
        aggregator.sendpost()
        
    except Exception, e:
        logging.error('Erro main:'+ str(e))

    finally:
    	logging.warning('------Fim--- %s', datetime.today())