#!/usr/bin/python

import bluetooth
import time

bd_addr = "00:06:66:7A:D1:05"

port = 1

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("push")

time.sleep(2)
sock.close()
