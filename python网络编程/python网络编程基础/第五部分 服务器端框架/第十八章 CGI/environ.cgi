#!/usr/bin/env  python
import cgitb
cgitb.enable()
 

import cgi
print 'Content-type:text/html'
print

print """<html>
<head>
<title>cgi environment </title>
</head>
<body>"""

cgi.print_environ()
print "</body></html>"
