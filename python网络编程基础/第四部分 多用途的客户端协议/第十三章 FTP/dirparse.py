#!/usr/bin/env python
from ftplib import FTP
class DirEntry:
	def __init__(self,line):
		self.parts = line.split(None,8)
	def isvaild(self):
		return len(self.parts)>=6
	def gettype(self):
		return seelf.parts[0][0]
	def getfilename(self):
		if self.gettype()!='1':
			return self.parts[-1]
		else:
			return self.parts[-1].split('->',1)[0]
	def getlinkdest(self):
		if self.gettype() =='1':
			return self.parts[-1].split('->',1)[0]
		else:
			raise RuntimeError,'getlinkdest() called on non-link item'
	class DirScanner(dict):
		def addline(self,line):
			obj = DirEntry(line)
			if obj.isvaild():
				self[obj.getfilename()] = obj
	f = FTP('ftp.kernel.org')
	f.login()
	f.cwd('/pub/linux/kernel')
	d = DirScanner()
	f.dir(d.addline)
 	print '%d entries:' %len(d.keys())
	for key ,value in d.items():
		print '%s:type %s'%(key,value.gettype())
	f.quit()
