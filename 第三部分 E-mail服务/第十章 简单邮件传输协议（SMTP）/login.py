#!/usr/bin/env python
import sys,smtplib,socket
from getpass import getpass
if len(sys.argv)<4:
	print 'Syntax : %s server fromaddr toaddr '%sys.argv[0]
server = sys.argv[1]
fromaddr = sys.argv[2]
toaddrs = sys.argv[3]
message = 'linlin'
sys.stdout.write('enter username:')
username = sys.stdin.readline().strip()
password = getpass('enter password')

try:
	s= smyplib.SMTP(server)
	try:
		s.login(username.password)
	except smtplib.SMTPExcetion,e:
		print 'faild:',e
	s.sendmail(fromaddr,toaddrs,message)




except(socket.gaierror,socket.error,socket.herror,smtplib.SMTPException),e:
	print e
	sys.exit(2)
else:
	print 'success'

