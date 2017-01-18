#!/usr/bin/env python
from SimpleXMLRPCServer import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler
from SocketServer import ForkingMixIn
class Math:
	def pow(self,x,y):
		return x**y
	def hex(sel,x):
		return '%x'%x
class ForkingServer(ForkingMixIn,SimpleXMLRPCServer):
	pass
serveraddr = ('',8765)
srvr = ForkingServer(serveraddr,SimpleXMLRPCRequestHandler)
srvr.register_instance(Math())
srvr.register_introspection_functions()
srvr.serve_forever()
