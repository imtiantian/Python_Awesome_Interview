class Solution:
    def NumberOf1(self, n):
        # write code here
        if n<0:
            s=bin(2**32+n)
        else:
            s=bin(n)
        counter=0
        for i in s:
            if i=='1':
                counter+=1
        return counter

