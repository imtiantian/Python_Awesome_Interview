#-*-coding=utf-8-*-
class Time:
    def __init__(self):
        self.hour=0
        self.minute=0
        self.second=0
    def printMilitary(self):
        print "%.2d%.2d%.2d"%(self.hour,self.minute,self.second)
    def printStandard(self):
        standardTime =""
        if self.hour==0 or self.hour==12:
            standardTime+="12:"
        else:
            standardTime+="%d:"%(self.hour%12)
        standardTime+="%.2d:%.2d"%(self.minute,self.second)
        if self.hour<12:
            standardTime+="AM"
        else:
            standardTime+="PM"
        print standardTime
