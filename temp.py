#!/usr/bin/python

import Adafruit_DHT as dht
import time
import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['temperature-station']
readings = db.readings

reading = 0

def read():
	global reading
	global readings

	if reading == 1:
		time.sleep(3)

	h,t =  dht.read_retry(dht.DHT22, 19)

	readings.insert_one({
		"date": datetime.datetime.utcnow(),
		"temperature": t,
		"humidity" : h
	})

	reading = 0

	return (h, t)
