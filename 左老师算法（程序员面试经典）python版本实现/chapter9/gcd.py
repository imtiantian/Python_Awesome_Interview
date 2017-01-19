def gcd(m,n):
    return n==0 and m or gcd(n,m%n)
print(gcd(15,5))
