# 2 1 6 4 5 2 7
l=[int(x) for x in raw_input().split()]
h=[l[0]]
for i in xrange(1,len(l)):
    if h[-1]>l[i] :
        head=0
        tail=len(h)-1
        while head < tail:
            mid = (head + tail) / 2
            if h[mid] >= l[i]:
                tail = mid
            else:
                head = mid + 1
        h[head]=l[i]

    else:
        h.append(l[i])
print len(h)
