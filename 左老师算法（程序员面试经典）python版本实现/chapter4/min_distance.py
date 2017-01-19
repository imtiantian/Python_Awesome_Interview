l=[[int(x) for x in raw_input().split()] for y in range(4)]

def min_distance(l):
    dp=[[0 for i in range(4)] for j in range(4)]
    dp[0][0]=l[0][0]
    row=len(l)
    col=len(l[0])
    for i in range(row):
        dp[0][i]=dp[0][i-1]+l[0][i]
    for i in range(col):
        dp[i][0]=dp[i-1][0]+l[i][0]
    for i in range(1,row):
        for j in range(1,col):
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])+l[i][j]
    return dp[row-1][col-1]

print min_distance(l)

'''
test data
1 3 5 9
8 1 3 4
5 0 6 1
8 8 4 0
'''