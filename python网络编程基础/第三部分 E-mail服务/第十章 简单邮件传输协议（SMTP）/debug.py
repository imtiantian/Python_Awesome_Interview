#!/usr/bin/env python
import sys,smtplib
if len(sys.argv)<4:
	print 'Syntax : %s server fromaddr toaddr '%sys.argv[0]
	sys.exit(255)
server = sys.argv[1]
fromaddr = sys.argv[2]
toaddrs = sys.argv[3]
message = 'linlin'

try:
	
	s = smtplib.SMTP(server)
	s.set_debuglevel(1)
	s.sendmail(fromaddr,toaddrs,message)
except (socket.gaierror,socket.error,socket.herror,smtplib.SMTPException),e:
	print 'error:'
	print e
	sys.exit(1)
else:
	print 'success'
print 'sucsess'
