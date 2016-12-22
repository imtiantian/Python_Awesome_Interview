#!/usr/bin/env python
import sys,struct
def htons(num):
	return struct.pack('!H',num)
def htonl(num):
	return struct.pack('!I',num)
def ntohs(num):
	return struct.unpack('!H',data)[0]
def ntohl(data):
	return struct.unpack('!I',data)[0]
def sendstring(data):
	return htonl(len(data))+data
print 'enter a string:'
sys.stdin.readline().strip()
print repr(sendstring(str))
