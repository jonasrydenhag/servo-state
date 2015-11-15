#!/usr/bin/python

import Adafruit_DHT as dht

h,t = dht.read_retry(dht.DHT22, 19)
print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t,h)

