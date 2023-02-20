"""
Write a program to determine how many distinct ways there are
to create a max heap from a list of N given integers.
For example, if N = 3, and our integers are [1, 2, 3],
there are two ways, shown below.
  3      3
 / \    / \
1   2  2   1
*Source of code
https://www.geeksforgeeks.org/number-ways-form-heap-n-distinct-integers/
"""

# to calculate nCk
def choose(n, k, nck):
    if (k > n):
        return 0
    if (n <= 1):
        return 1
    if (k == 0):
        return 1
 
    if (nck[n][k] != -1):
        return nck[n][k]
 
    answer = choose(n - 1, k - 1, nck) + choose(n - 1, k, nck)
    nck[n][k] = answer
    return answer

# find maximum number of heaps for n
def numberOfHeaps(n, dp, log2, nck):
    if (n <= 1):
        return 1
 
    if (dp[n] != -1):
        return dp[n]
 
    left = getLeft(n, log2)
    ans = (choose(n - 1, left, nck) * numberOfHeaps(left, dp, log2, nck)) * (numberOfHeaps(n - 1 - left, dp, log2, nck))
    dp[n] = ans
    return ans

# calculate l for give value of n
def getLeft(n, log2):
    if (n == 1):
        return 0
 
    h = log2[n]
 
    # max number of elements that can be present in the
    # hth level of any heap
    numh = (1 << h) #(2 ^ h)
 
    # number of elements that are actually present in
    # last level(hth level)
    # (2^h - 1)
    last = n - ((1 << h) - 1)
 
    # if more than half-filled
    if (last >= (numh // 2)):
        return (1 << h) - 1 # (2^h) - 1
    else:
        return (1 << h) - 1 - ((numh // 2) - last)

def Solution(n):
    MAXN = 105
    dp = [0] * MAXN
    nck = [[0 for i in range(MAXN)] for j in range(MAXN)]
    log2 = [0] * MAXN
    
    for i in range(n+1):
        dp[i] = -1
 
    for i in range(n+1):
        for j in range(n+1):
            nck[i][j] = -1
 
    currLog2 = -1
    currPower2 = 1
 
    # for each power of two find logarithm
    for i in range(1,n+1):
        if (currPower2 == i):
            currLog2 += 1
            currPower2 *= 2
        log2[i] = currLog2
    return numberOfHeaps(n, dp, log2, nck)

# Return 2
print(Solution(3))
# Return 3
print(Solution(4))
# Return 3360
print(Solution(10))