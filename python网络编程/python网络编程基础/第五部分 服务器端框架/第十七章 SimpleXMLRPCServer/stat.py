#!/usr/bin/env python
from SimpleXMLRPCServer import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler
from SocketServer import ForkingMixIn
import time
class Stats:
	def getstat(self):
		return self.callstats
	def getruntime(self):
		return time.time()-self.starttime()
	def failure(self):
		return RuntimeError,'always raises an error'
class Math(Stats):
	def __init__(self):
		self.callstats = {'pow':0,'hex':0}
		self.starttime = time.time()
	def pow(self,x,y):
		self.callstat['pow']+=1
		return pow(x,y)
	def hex(sel,x):
		self.callstat['hex']+=1
		return '%x'%x
class ForkingServer(ForkingMixIn,SimpleXMLRPCServer):
	pass
serveraddr = ('',8765)
srvr = ForkingServer(serveraddr,SimpleXMLRPCRequestHandler)
srvr.register_instance(Math())
srvr.register_introspection_functions()
srvr.serve_forever()
