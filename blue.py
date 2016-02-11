#!/usr/bin/python

import bluetooth
import time
import subprocess
import sys

bd_addr = "00:06:66:7A:D1:05"
channel = 1

proc = None

connectProblemNr = 0
keepAlive = 1

def connect():
	global proc
	global connectProblemNr
	global keepAlive

	if (connectProblemNr > 1):
		print "too many problems"
		keepAlive = 0
		return

	cmd = "rfcomm connect /dev/rfcomm1 %s %s" % (bd_addr, channel)

	proc = subprocess.Popen(
		cmd,
		shell=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE
	)

	print "-comm-s"
	outs, errs = proc.communicate()
	print "-comm-e"

	if (errs == "Can't connect RFCOMM socket: Host is down\n"):
		connectProblemNr += 1
		print "we have a problem"
		time.sleep(2)
		connect()
	else:
		connectProblemNr = 0

try:
	connect()

	while keepAlive:
		time.sleep(1)
		print "-poll-s"
		print proc.poll()
		print "-poll-e"
		if (proc.poll() == 0):
			print "gone reconnect"
			connect()

except KeyboardInterrupt:
	print "Quit"
except:
	print "Unexpected error:", sys.exc_info()[0]
finally:
	if (proc.poll() != 0):
		proc.kill()

print "done"
