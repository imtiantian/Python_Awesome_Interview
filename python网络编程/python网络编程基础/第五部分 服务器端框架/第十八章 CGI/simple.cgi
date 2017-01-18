#!/usr/bin/env python
import cgitb
cgitb.enable()

import time
print 'Content-type:text/html'
print
print """<html>
<head>
<title>simple cgi  </title>
</head>
<body>
the time is %s.
</body>
</html>"""%time.strftime("%I:%M:%S %P %Z")
print
