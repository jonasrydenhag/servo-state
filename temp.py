#!/usr/bin/python

import Adafruit_DHT as dht
import time
import pymongo
import datetime
from pymongo import MongoClient
import sys

client = MongoClient('localhost', 27017)
db = client['temperature-station']
readings = db.readings

reading = 0

def read():
	global reading
	global readings

	if reading == 1:
		time.sleep(3)
	reading = 1

	h,t = dht.read_retry(dht.DHT22, 19)

	date = datetime.datetime.utcnow()

	readings.insert_one({
		"date": date,
		"temperature": t,
		"humidity" : h
	})

	reading = 0

	return (h, t, date)

if len(sys.argv) > 1 and sys.argv[1] == "read":
	h,t,date = read()
	print '{0},{1},{2}'.format(h,t,date)
