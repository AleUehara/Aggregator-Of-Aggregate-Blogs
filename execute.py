#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
import logging
import aggregator_env_variables
from linklog.execute import Linklog
from atoananet.execute import AToaNaNet
from datetime import date, timedelta, datetime


logging.basicConfig(filename=os.environ['AGGREGATOR_LOG'],level=logging.WARNING)

def call_atoananet():
        print 'atoa'
        atoananet = AToaNaNet()
        atoananet.login()
        atoananet.sendpost()

def call_linklog():
	print 'linklog'
	Linklog().sendpost()

def main():
	call_atoananet()
	#call_linklog()

if __name__ == "__main__":
    try:
        logging.warning('------Inicio--- %s', datetime.today())
        main()
    except Exception, e:
        print e		
        print os.environ['AGGREGATOR']
        logging.error('Erro main:', e)
    
    finally:
    	logging.warning('------Fim--- %s', datetime.today())


#http://www.linklog.com.br/links/enviar