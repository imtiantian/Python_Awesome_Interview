# from collections import Counter
# li =['a','b','c','d','a']
# a= Counter(li)
# print a
# print len(set(li))
# print "{0}:{1}".format(a.values(),a.keys())
import pprint
ll=[[1,2,3],[4,5,6],[7,8,9]]
a=pprint.PrettyPrinter(width=30)
a.pprint(ll)
print ll