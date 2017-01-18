#!/usr/bin/env python
import sys,urllib2,urllib
zipcode = sys.argv[1]
url = ''
data = urllib.urlcode([('query','zipcode')])
req =  urllib2.Request(url)
fd = urllib2.urlopen(req,data)
while 1:
	data = fd.read(1024)
	if not len(data):
		break
	sys.stdout.write(data)

