#!/usr/bin/env python
import gopherlib ,sys
host = sys.argv[1]
file = sys.argv[2]
f = gopherlib.send_selertor(file,host)
for line in f.readlines():
	sys.stdout.write(line)
