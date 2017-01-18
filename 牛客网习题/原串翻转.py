# -*- coding:utf-8 -*-
class Reverse:
    def reverseString(self, iniString):
        # write code here
        print iniString
        iniString=list(iniString)
        after=iniString[::-1]
        after=''.join(after)
        return after
a=Reverse()
print a.reverseString("as ba ac")