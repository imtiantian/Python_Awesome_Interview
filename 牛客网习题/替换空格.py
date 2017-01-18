# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
      s = list(s)
      le = len(s)
      for i in range(le):
      	if s[i] == " ":
        	s[i] = "%20"
        else:
        	pass
      return "".join(s)
    #请实现一个函数，将一个字符串中的空格替换成“%20”。
        # 例如，当字符串为We Are Happy.
        # 则经过替换之后的字符串为We%20Are%20Happy