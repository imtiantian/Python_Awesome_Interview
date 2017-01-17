#!/usr/bin/env python
from ftplib import FTP
f = FTP('ftp.ibiblio.org')
print 'welcome',f.getwelcome()
f.login()
print 'CWD:',f.pwd()
f.quit()
