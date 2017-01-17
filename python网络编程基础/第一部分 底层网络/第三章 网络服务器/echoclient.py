#!/usr/bin/env python 
import socket,sys
port = 51423
host = 'localhost'
data = "x"*1048
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
bytewritten = 0
while bytewritten <len(data):
	startpos = bytewritten
	endpos = min (bytewritten+1024,len(data))
	bytewritten +=s.send(data[startpos:endpos])
	sys.stdout.write('write%dbytes\r'%bytewritten)
	sys.stdout.flush()
s.shutdown(1)
print 'all data sent'
while 1:
	buf = s.recv(1024)
	if not len (buf):
		break
	sys.stdout.write(buf)
