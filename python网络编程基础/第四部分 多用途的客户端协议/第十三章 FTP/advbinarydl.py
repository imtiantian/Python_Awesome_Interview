#!/usr/bib/env python
from ftplib import FTP
import sys 
f = FTP('ftp.kernel.org')
f.login()
f.cwd('/pub/linux/kernel/v1.0')
f.voidcmd('TYPE I')

datasock,estsize = f.ntransfercmd('RETR linux-1.0.tar.gz')
transbytes = 0
fd = open ('linux-1.0.tar.gz','wb')
while 1:
	buf = datasock.recv(2048)
	if not len(buf):
		break
	fd.write(buf)
	transbytes +=len(buf)
	sys.stdout.write('recevid %d'%transbytes)

	if estsize:
		sys.stdout.write('of %d bytes(%.1f%%)\r'%\
			(estsize,100.0*float(transbytes)/float(estszie)))
	else:
		sys.stdout.write('bytes\r')
	sys.stdout.flush()
sys.stdout.write('\n')
fd.close()
datasock.close()
f.voidresp()
f.quit()
