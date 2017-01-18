#!/usr/bin/env python
import MySQLdb
print 'connecting ...'
dbh = MySQLdb.connect(db = 'mysql')
print 'successful'
dbh.close()
