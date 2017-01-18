#-*-coding=utf-8-*-
#暴力解法
def celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u==v:continue
            if G[u][v]:break
            if not G[v][u]:break
        else:
            return u
    return None
from random import randrange
m=100
G=[[randrange(2)for i in range(m)]for i in range(m)]
c=randrange(m)
for i in range(m):
    G[i][c]=True
    G[c][i]=False
print celeb(G)
# print G