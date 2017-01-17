#!/usr/bin/env python
import sys,urllib2,getpass
class TerminalPassword(urllib2.HTTPPasswordMgr):
	def find_user_password(self,realm,authuri):
		retval = urllib2.HTTPPasswordMgr.find_user_password(self,realm,authuri)
	if retval[0] ==None and retval[1]==None:
		sys.stdout.write('login require for %s at %s')%(realm,authuri)
		sys.stdout.write('username:')
		username = sys.stdin.readline().strip()
		password = getpass.getpass().strip()
		return (username,password)
	else:
		return retval
req = urllib2.Request(sys.argv[1])
opener =urllib2.build_opener(urllib2.HTTPBasicAuthHandler(TerminalPassword()))
fd = opener.open(req)
print 'retrieved',fd.geturl()
info =  fd.info()
for key ,value in info.items():
	print '%s = %s'%(key,value)
