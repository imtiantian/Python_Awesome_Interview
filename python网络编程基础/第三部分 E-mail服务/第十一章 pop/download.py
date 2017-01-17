#!/usr/bin/env python
import getpass ,poplib ,sys ,email
(host,user,dest) = sys.argv[1:]
passwd = getpass.getpass()

destfd = open(dest,"at")

p = poplib.POP3(host)
try:
	p.user(user)
	p.pass_(passwd)
except poplib.error_proto,e:
	print 'login failed:',e
	sys.exit(1)
for item in p.list()[1]:
	number,octets = item.split(' ')
	print "down msg %s(%s bytes)"%(number,octets)
	lines = p.retr(number)[1]
	msg = email.message_from_string('\n'.join(lines))
	destfd.write(msg.as_string(unixfrom =1))
	destfd.write('\n')
p.quit()
destfd.close()
