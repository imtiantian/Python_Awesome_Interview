# -*- coding:utf-8 -*-
#菲薄那列方法
#可以知道f(n)有f(n-1)和f(n-2)种方法
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 1

        elif number <= 2:
            return number

        else:
            a, b = 1, 2
            for i in range(2, number):
                a, b = b, a + b
            return b
    #一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。