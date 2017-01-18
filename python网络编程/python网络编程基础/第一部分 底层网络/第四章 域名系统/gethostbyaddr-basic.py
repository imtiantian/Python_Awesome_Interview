#!/usr/bin/env python
import sys,socket
try:
	result = socket.gethostbyaddr(sys.argv[1])
	print 'p name:'
	print ' '+result[0]
	print 'address:'
	for item in result[2]:
		print " "+item
except socket.herror,e:
	print 'not find'
