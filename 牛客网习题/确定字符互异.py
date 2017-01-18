# -*- coding:utf-8 -*-
class Different:
    def checkDifferent(self, iniString):
        # write code here
        length = len(iniString)
        for i in range(length):
            for j in range(i+1, length):
                if iniString[i] == iniString[j]:
                    return False
        return True
a=Different()
print a.checkDifferent('asdas')
print a.checkDifferent("D-5H0F6T%Z?QM9,\72:[A8X! ;YJ#")