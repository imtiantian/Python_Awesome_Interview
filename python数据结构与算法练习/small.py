from random import randrange
seq = [randrange(100)for i in range(1000)]
dd=float('inf')
for x in seq:
    for y in seq:
        if x==y:continue
        d=abs(x-y)
        if d<dd:
            xx,yy,dd=x,y,d
print xx,yy
#时间复杂度N*N
