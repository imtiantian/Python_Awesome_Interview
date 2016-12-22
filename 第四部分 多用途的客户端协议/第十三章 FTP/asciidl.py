#!/usr/bin/env python
from ftplib import FTP

def writeline(data):
	fd.write(data + '\n')

f =  FTP('ftp.kernel.org')
f.login()
f.cwd('/pub/linux/kernel')
fd = open ('README','wt')
f.retrlines('RETR README',writeline)
fd.close()
f.quit()

