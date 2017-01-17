#!/usr/bin/env python
from SimpleXMLRPCServer import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler
from SocketServer import ForkingMixIn
class Math:
	def pow(self,x,y):
		return pow(x,y)
	def hex(sel,x):
		return '%x'%x
	def sortlist(self,l):
		l = list(l)
		l.sort()
		return l
class ForkingServer(ForkingMixIn,SimpleXMLRPCServer):
	pass
serveraddr = ('',8765)
srvr = ForkingServer(serveraddr,SimpleXMLRPCRequestHandler)
srvr.register_instance(Math())
srvr.register_introspection_functions()
srvr.register_function(int)
srvr.register_function(list.sort)
srvr.serve_forever()
