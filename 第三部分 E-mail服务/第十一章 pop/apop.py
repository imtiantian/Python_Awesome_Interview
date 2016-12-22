#!/usr/bin/env python
import getpass ,poplib,sys
(host,user)  = sys.argv[1:]
passwd  = getpass.getpass()
p  =poplib.POP3(host)
try:
	print 'apop'
	p.apop(user,passwd)
except poplib.error_proto:
	print 'standard'
	try:
		p.user(user)
		p.pass_(passwd)
	except poplib.error_proto,e:
		print 'login error:',e
		sys.exit(1)
status = p.stat()
print 'mailbox has %d message for a total of  %d bytes' %(status[0])
p.quit()
