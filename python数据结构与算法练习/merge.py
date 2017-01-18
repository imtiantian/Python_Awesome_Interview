import time,cProfile
def mergesort(seq):
    mid = len(seq)//2
    lft,rgt = seq[:mid],seq[mid:]
    if len(lft)>1:lft = mergesort(lft)
    if len(rgt)>1:rgt = mergesort(rgt)
    res=[]
    while lft and rgt:
        if lft[-1]>=rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) +res
if __name__=='__main__':
    start = time.clock()
    L=[3,2,9,4,5,7,6,8]
    print L
    print mergesort(L)
    end  = time.clock()
    print end-start
    #平均时间0.000114540953523