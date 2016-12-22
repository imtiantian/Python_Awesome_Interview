#!/usr/bin/env python
import sys,DNS
def hierquery(qstring,qtype):
	reqobj = DNS.Request()
	try:
		answerobj = reqobj.req(name = qstring ,qtype = qtype)
		answers=[x['data']for x in answerobj.answers if x['type']==qtype]
	except DNS.base.dNSError:
		answers=[]
	if len (answers):
		return answers
	else:
		remainder = qstring('.',1)
