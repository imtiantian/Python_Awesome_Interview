#-*- coding=utf-8 -*-
# 二分查找
def binary_search(list,item):
    first=0
    last=len(list)-1
    found=False
    while first<=last and not found:
        mid=(first+last)//2
        if list[mid]==item:
            found=True
        else:
            if item<list[mid]:
                last=mid-1
            else:
                first=mid+1
    return found
list=[0,1,2,8,13,17,19,32,42]
print (binary_search(list,3))
print (binary_search(list,13))