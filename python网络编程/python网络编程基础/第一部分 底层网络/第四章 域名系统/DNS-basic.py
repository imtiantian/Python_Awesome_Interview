#!/usr/bin/env python
import DNS ,sys
query = sys.argv[1]
DNS.DiscoverNameServers()
reqobj = DNS.Request()
answerobj = reqobj.req(name = query,qtype = DNS.Type.ANY)
if not len(answerobj.answers):
	print 'Not found'
for item in answerobj.answers:
	print "%s-%s"%(item['typename'],item['data'])
