#!/usr/bin/env python
import sys,urllib2

req = urllib2.Request(sys.argv[1])

try:
	fd = urllib2.urlopen(req)

except urllib2.URLError,e:
	print 'retrieving data:',e
	sys.exit(1)
print 're',fd.geturl()
info = fd.info()
for key,value in info.items():
	print '%s=%s'%(key,value)
