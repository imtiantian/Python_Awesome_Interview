#!/usr/bin/env python
import socket,sys
from OpenSSL import SSL
ctx  =SSL.Context(SSL.SSLv23_METHOD)
print 'creat'
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'done'


ssl = SSL.Connection(ctx,s)

print 'connect'
s.connect(('www.openssl.org',443))
print 'done'

print 'request'
ssl.sendall("GET / HTTP/1.0\r\n\r\n")

while 1:
	try:
		buf = ssl.recv(4096)
	except SSL.ZeroReturnError:
		break
	sys.stdout.write(buf)
ssl.close()
