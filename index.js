#!/usr/bin/python

def changeState():
	import datetime

	newSwitch = {
		"date": datetime.datetime.utcnow()
	}

	import sys
	import pymongo
	from pymongo import MongoClient

	client = MongoClient('localhost', 27017)
	db = client['temperature-station']
	switches = db.switches

	for switch in switches.find().limit(1).sort("date", -1):
		if switch['state'] == 'on':
			newSwitch['state'] = 'off'
		elif switch['state'] == 'off':
			newSwitch['state'] = 'on'
		else:
			sys.exit()

	switches.insert_one(newSwitch)

	if newSwitch['state'] == 'on':
		import singleLed
		singleLed.run()
