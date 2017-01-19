import sys


def min_coins(arr, aim):
    if  len(arr) == 0 or aim < 0:
        return -1
    n = len(arr)
    max = sys.maxint
    dp = [[0 for y in range(aim+1)] for x in range(n)]
    for j in range(1, aim+1):
        dp[0][j] = max
        if j-arr[0] >= 0 and dp[0][j-arr[0]] != max:
            dp[0][j] = dp[0][j-arr[0]]+1
    print dp
    for i in range(1, n):
        for j in range(1, aim+1):
            left = max
            if j-arr[i] >= 0 and dp[i][j-arr[i]] != max:
                left = dp[i][j-arr[i]]+1
            dp[i][j] = min(left, dp[i-1][j])
    print dp
    return dp[n-1][aim] != max and dp[n-1][aim] or -1
    # return dp[n-1][aim]

# arr = [10, 100, 2, 5, 5, 5, 10, 1, 1, 1, 2, 100]
array = [5, 2, 3]
target = 5
print(min_coins(array, target))


