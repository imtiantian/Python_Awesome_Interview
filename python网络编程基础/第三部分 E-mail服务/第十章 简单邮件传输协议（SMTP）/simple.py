#!/usr/bin/env python
import sys,smtplib
if len(sys.argv)<4:
	print 'Syntax : %s server fromaddr toaddr '%sys.argv[0]
server = sys.argv[1]
fromaddr = sys.argv[2]
toaddrs = sys.argv[3]
message = 'linlin'
s = smtplib.SMTP(server)
s.sendmail(fromaddr,toaddrs,message)
print 'sucsess'
