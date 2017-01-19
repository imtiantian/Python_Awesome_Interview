def fibo(n):
    if n==1 or n==2:
        return 1
    return fibo(n-1)+fibo(n-2)

def cow(n):
    if n<1:
        return 0
    if n==1 or n==2 or n==3:
        return n
    return cow(n-1)+cow(n-3)

def dynamic_cow(n):
    if n<1:
        return 0
    l=[1,2,3]
    for i in range(3,n):
        l.append(l[i-1]+l[i-3])
    return l[n-1]

def dynamic_fibo(n):
    l=[1,1]
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    return l[n-1]

print fibo(5)
print '----------'
print dynamic_fibo(5)

print cow(0)
print dynamic_cow(6)


# fibo
#1 1 2 3 5 8 13