import time
def gnomesort(seq):
    i=0
    while i<len(seq):
        if i==0 or seq[i-1]<=seq[i]:
            i+=1
        else:
            seq[i-1],seq[i]=seq[i],seq[i-1]
            i-=1
ll=[1,2,4,5,3,1]
print ll
start = time.clock()
gnomesort(ll)
print ll
end = time.clock()
print ('%.10f')%(end-start)
#平均时间0.0000406436
