#!/usr/bin/env python
import sys,smtplib,socket
if len(sys.argv)<4:
	print 'Syntax : %s server fromaddr toaddr '%sys.argv[0]
server = sys.argv[1]
fromaddr = sys.argv[2]
toaddrs = sys.argv[3]
message = 'linlin'
try:
	s=  smtplib.SMTP(server)
	code = s.ehlo()[0]
	usesesmtp =1
	if not (200<=code<=299):
		usesesmtp = 0
		code = s.helo()[0]
		if not (200<=code<=299):
			raise SMTPHeloError(code,resp)
	if usesesmtp and s.has_extn('size'):
		print 'max msg size is:',s.esmtp_features['size']
		if len(message) > int(s.esmtp_features['size']):
			print 'msg too large'
			sys.exit(2)
	s.sendmail(fromaddr,toaddrs,message)
except(socket.gaierror,socket.error,socket.herror,smtplib.SMTPException),e:
	print e
	sys.exit(1)
else:
	print 'success'

