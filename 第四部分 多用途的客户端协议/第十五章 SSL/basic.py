#!/usr/bin/env python 
import sys,socket
def sendall(s,buf):
	bytewritten = 0 
	while bytewritten < len (buf):
		bytewritten += s.write(buf[bytewritten:])
print 'creat'
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'done'

print  'connect'

s.connect(('www.openssl.org',443))

print 'done'

print 'establish'
ssl  = socket.ssl(s)
print 'done'

print 'request'
sendall(ssl,"GET / HTTP/1.0\r\n\r\n")
print 'done'

s.shutdown(1)

while 1:
	try:
		buf = ssl.read(1024)
	except socket.sslerror,err:
		if (err[0]) in [socket.SSL_ERROR_ZERO_RETURN,socket.SSL_ERROR_EOF]:
			break
	elif (err[0]) in  [socket.SSL_ERROR_WANT_READ,socket.SSL_ERROR_WANT_WRITE]:
			continue
		raise
	if len(buf)==0:
		break
	sys.stdout.write(buf)
s.close()


