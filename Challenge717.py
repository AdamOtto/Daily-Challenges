"""
A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to
build the nth house with kth color, return the minimum cost which achieves this goal.
"""
def Solution(ar, n, k):
    if n == 0:
        return 0
    
    dp = [[0 for i in range(k)] for j in range(n)]
    
    for i in range(k):
        dp[0][i] = ar[0][i]
    
    for i in range(1, n):
        for j in range(k):
            dp[i][j] = getMin(dp, i, j) + ar[i][j]
    return min(dp[n - 1])

def getMin(dp, ind, cur):
    retVal = max(dp[ind - 1])
    for i in range(len(dp[ind - 1])):
        if i != cur:
            retVal = min(retVal, dp[ind - 1][i])
    return retVal

# Return 4
in1 = [[1,1,1,1],
       [2,2,2,2],
       [1,1,1,1]]
print(Solution(in1, 3, 4))

# Return 3
in1 = [[1,8,9,1,4],
       [4,4,1,5,6],
       [3,7,5,1,3]]
print(Solution(in1, 3, 5))

# Return 6
in1 = [[6,8,9,1,4],
       [4,4,5,1,6],
       [3,7,5,1,3]]
print(Solution(in1, 3, 5))