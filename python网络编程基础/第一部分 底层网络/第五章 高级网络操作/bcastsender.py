#!/usr/bin/env python
import socket,sys
dest = ('<broadcast>',51423)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket,SO_BROADCAST,1)
s.sendto('hello',dest)
print 'looking for'
while 1:
	(buf,address) = s.recvfrom(2048)
	if not len(buf):
		break
	print 'recv from %s:%s'%(address,buf)
	

