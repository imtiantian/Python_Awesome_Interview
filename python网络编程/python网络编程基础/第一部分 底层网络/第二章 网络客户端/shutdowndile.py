#!/usr/bin/env python
import sys,socket,time
host     = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,e:
	print 'creating socket error:%s'%e
	sys.exit(1)

try:
	port = int(textport)
except socket.error,e:
	print "not find port:%s"%e
	sys.exit(1)

try :
	s.connect((host,port))
except socket.gaierror,e:
	print 'error addr connect :%s'%e
	sys.exit(1)
except socket.error,e:
	print 'error connect :%s'%e
	sys.exit(1)
fd = socket.makefile('rw',0)
print 'sleeping'
time.sleep(10)
print 'continuing'
try:	
	fd.write('GET %s HTTP/1.0 \r\n\r\n'%filename)
except socket.error,e:
	print 'error sending data:%s'%e
	sys.exit(1)
try:
	fd.flush()
except socket.error,e:
	pritn 'error sending data'
	sys.exit(1)
try:
	s.shutdown(1)
	s.close()
except socket.error,e:
	print 'error send finish'
	sys.exit(1)

while 1:
	try:
		buf = fd.read(1024)
	except socket.error,e:
		print 'error recving data:%s'%e
		sys.exit(1)
	if not len(buf):
		break
	sys.stdout.write(buf)
