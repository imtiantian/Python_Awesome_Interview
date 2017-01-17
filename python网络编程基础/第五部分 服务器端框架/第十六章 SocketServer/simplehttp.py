#!/usr/bin/env python
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

serveraddr = ('',8765)
srvr = HTTPServer(serveraddr,SimpleHTTPRequestHandler)
srvr.serve_forever()
