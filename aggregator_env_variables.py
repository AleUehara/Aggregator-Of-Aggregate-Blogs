#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os

os.environ['AGGREGATOR']        = os.path.dirname(__file__)
os.environ['AGGREGATOR_CONFIG'] = os.path.join(os.environ['AGGREGATOR'], "aggregator.cfg")
os.environ['AGGREGATOR_LOG']    = os.path.join(os.environ['AGGREGATOR'], "log", "aggregator.log")