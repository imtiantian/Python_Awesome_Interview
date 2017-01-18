#!/usr/bin/env python
from HTMLParser import HTMLParser
import sys
class TitleParser(HTMLParser):
	def __init__(self):
		self.title = ''
		self.readingtitle =0
		HTMLParser.__init__(self)
	def handle_starttag(self,tag,attrs):
		if tag =='title':
			self.readingtitle =1
	def handle_data(self,data):
		if self.readingtitle:
			self.title +=data
	def handle_endtag(self,tag):
		if tag =='title':
			self.readingtitle =0
	def gettitle(self):
		return self.title
fd = open(sys.argv[1])
tp = TitleParser()
tp.feed(fd.read())
print 'title is: ',tp.gettitle()
