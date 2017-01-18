#-*-coding=utf-8-*-
#math模块
# import math
# n =math.sqrt(900)
# nn = math.pow(2,10)
# print n,nn
#模拟投掷
# import random
# time1=0
# time2=0
# time3=0
# time4=0
# time5=0
# time6=0
# for i in range(1,6000):
#     face = random.randrange(1,7)
#     # print "%2d"%(random.randrange(1,7)),
#     # if i % 5 == 0:
#     #     print
#     if face ==1:
#         time1+=1
#     elif face ==2:
#         time2+=1
#     elif face ==3:
#         time3+=1
#     elif face ==4:
#         time4+=1
#     elif face ==5:
#         time5+=1
#     elif face ==6:
#         time6+=1
#     else:
#         print "none"
# print "face %10s"%"times"
# print "1 %10d"%time1
# print "2 %10d"%time2
# print "3 %10d"%time3
# print "4 %10d"%time4
# print "5 %10d"%time5
# print "6 %10d"%time6
#全局变量和局部变量
# x=1
# def a():
#     x=25
#     print x
#     x+=1
#     print x
# a()
# def b():
#     global x
#     print x
#     x+=1
#     print x
# b()
# print x
# x=7
# print x