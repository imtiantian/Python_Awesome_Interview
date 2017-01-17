#!/usr/bin/env python
import xmlrpclib,code
url = 'http://localhost:8765/'
s = xmlrpclib.ServerProxy(url)
interp = code.InteractiveConsole({'s':s})
interp.interact('can use')
