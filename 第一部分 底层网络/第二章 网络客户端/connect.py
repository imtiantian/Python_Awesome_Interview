#!/usr/bin/env python
import socket
print 'creating  socket'
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'done'

print 'connecting to remote host'

s.connect(('www.baidu.com',80))
print 'done'

