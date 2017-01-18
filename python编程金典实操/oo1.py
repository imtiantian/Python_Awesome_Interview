#-*-coding=utf-8-*-
class Time:
    def __init__(self):
        self.__hour=0
        self.__minute=0
        self.__second=0
    def setTime(self):
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)
    def setHour(self,hour):
        if 0<=hour<24:
            self.__hour=hour
        else:
            raise ValueError
    def setMinute(self,minute):
        if 0<=minute<60:
            self.__minute=minute
        else:
            raise ValueError
    def setSecond(self,second):
        if 0<=second<60:
            self.__second=second
        else:
            raise ValueError
    def getHour(self):
        return self.__hour
    def getMinute(self):
        return self.__minute
    def getSecond(self):
        return self.__second
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
time=Time()
time.printMilitary()
time.printStandard()
