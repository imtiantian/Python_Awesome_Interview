#!/usr/bin/env python 
import sys,socket
def getipaddrs(hostname):
	result = socket.getaddrinfo(hostname,None,0,socket.SOCK_STREAM)
	return [x[4][0]for x in result]
hostname = socket.gethostname()
print 'host name',hostname
print 'fully:',socket.getfqdn(hostname)
try:
	print 'ip',','.join(getipaddrs(hostname))
except socket.gaierror,e:
	print 'not find ip:',e
