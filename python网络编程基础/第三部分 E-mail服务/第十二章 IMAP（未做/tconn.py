#!/usr/bin/env python
from twisted.internet import defer,reactor,protocol
from twisted.protocols.imap4 import IMAP4Client
import sys

class IMAPClient(IMAP4Client):
	def connectionMade(self):
		print 'l have sucessfully conn to the server'
		d = self.getCapablities()
		d.addCallback(self.gotcapabilities)
	def gotcapabilities(self,caps):
		if caps ==None:
			print 'Server did not return a capability list'
		else:
			for key ,value in caps.items():
				print "%s:%s"%(key,str(value))
		self.logout()
		reactor.stop()
class IMAPFactory(protocol.ClientFactory):
	protocol = IMAPClient
	
	def clientConnectionFailed(self,connector,reason):
		print 'Client connection failed :',reason
		reactor.stop()
reactor.connectTCP(sys.argc[1],143,IMAPFactory())
reactor.run()
