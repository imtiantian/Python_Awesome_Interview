#!/usr/bin/env python 
import urllib ,sys
f = urllib.urlopen(sys.argv[1])
while 1:
	buf = f.read(1024)
	if not len(buf):
		break
	sys.stdout.write(buf)
