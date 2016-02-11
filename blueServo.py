#!/usr/bin/python

import subprocess

rfcomm = "rfcomm1"
pushCmd = "push"

cmd = "echo '%s' > /dev/%s" % (pushCmd, rfcomm)
proc = subprocess.call(cmd, shell=True)

import setState
setState.changeState()
