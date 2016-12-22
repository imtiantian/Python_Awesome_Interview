#!/usr/bin/env python 
import sys
print 'welcome'
print 'enter a string'
sys.stdout.flush()
line = sys.stdin.readline().strip()
print 'you enterd %d'%len(line)
