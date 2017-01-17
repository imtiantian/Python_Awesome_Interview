#!/usr/bin/env python
from SocketServer import TreadingMixIn,TCPServer,StreamRequestHandler
import time
class TimeRequestHandler(StreamRequestHandler):
	def handle(self):
		req = self.rfilt.readline().strip()
			if req =='asctime':
				result = time.asctime()
			elif req == 'seconds':
				result = str(int(time.time()))
			elif req = 'rfc822':
				result = time.strftime
