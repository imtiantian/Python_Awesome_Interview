#!/usr/bin/env python
import socket
print 'creating  socket'
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'done'

print 'looking for port '
port = socket.getservbyname('http','tcp')
print 'done'






print 'connecting to remote host'

s.connect(('www.baidu.com',port))
print 'done'
print 'connect from',s.getsockname()
print 'connect to ',s.getpeername()
