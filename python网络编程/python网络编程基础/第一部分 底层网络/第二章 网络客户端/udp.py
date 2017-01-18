#!/usr/bin/env python
import sys ,socket
host = sys.argv[1]
textport = sys.argv[2]
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
	port = int(textport)
except ValueError:
	port = socket.getservbyname(textport,'udp')
s.connect((host,port))
print 'enter data to :'
data = sys.stdin.readline().strip()
s.sendall(data)
print 'looking for ,ctrl-c to die'
while 1:
	buf =s.recv(1024)
	if not len (buf):
		break
	sys.stdout.write(buf)
