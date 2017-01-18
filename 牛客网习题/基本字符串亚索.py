# -*- coding:utf-8 -*-
class Zipper:
    def zipString(self, iniString):
        # write code here
        result=""
        if len(iniString)<=0:
            return result
        count=1
        result+=iniString[0]
        for i in range(1,len(iniString)):
            if iniString[i]==iniString[i-1]:
                count+=1
            else:
                result+=str(count)
                result+=iniString[i]
                count=1
        result+=str(count)
        if len(result)>=len(iniString):
            return iniString
        else:
            return result