# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        ji=[]
        ou=[]
        for i in array:
            if i %2==0:
                ou.append(i)
            else:
                ji.append(i)
        array = ji+ou
        return array

a=Solution()
print a.reOrderArray([1,2,3,4,5,6])

#输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，
# 所有的偶数位于位于数组的后半部分，并保证奇数和奇数，
# 偶数和偶数之间的相对位置不变。
