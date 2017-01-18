#-*- coding=utf-8 -*-
# 顺序查找
def sequential_search(list,item):
    pos=0
    found=False
    while pos<len(list)and not found:
        if list[pos]==item:
            found=True
        else:
            pos=pos+1
    return found,pos
list=[1,2,32,8,17,19,13,0]
# print (sequential_search(list,3))
print (sequential_search(list,13))