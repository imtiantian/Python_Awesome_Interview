#!/usr/bin/env python
import socket,traceback
host =''
port = 51423
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
while 1:
	try:
		message,address = s. recvfrom(8192)
		print 'get data from ',address
		s.sendto(message,address)
	except (KeyboardInterrupt,SystemExit):
		raise
	except:
		traceback.print_exc()
