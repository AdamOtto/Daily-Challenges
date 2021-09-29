"""
Write a program to determine how many distinct ways there are
to create a max heap from a list of N given integers.

For example, if N = 3, and our integers are [1, 2, 3], there are two ways, shown below.

  3      3
 / \    / \
1   2  2   1

Notes: N = 4
    4        4        4
   / \      / \      / \
  3   2    3   1    2   3
 /        /        /
1        2        1

Help from:
https://www.geeksforgeeks.org/number-ways-form-heap-n-distinct-integers/
"""


def Solution(N):
    dp = []
    nck = []
    log2 = [0]* (N+1)
    
    for i in range(N + 1):
        dp.append(-1)
        nck.append([-1]*(N+1))

    currLog2 = -1
    currPower2 = 1
 
    for i in range(1, N+1):
        if (currPower2 == i):
            currLog2 += 1
            currPower2 *= 2
        log2[i] = currLog2
    return numberOfHeaps(N, dp, nck, log2)

def numberOfHeaps(n, dp, nck, log2):
    if (n <= 1):
        return 1
 
    if (dp[n] != -1):
        return dp[n]
 
    left = getLeft(n, log2)
    ans = (choose(n - 1, left, nck) * numberOfHeaps(left, dp, nck, log2)) * (numberOfHeaps(n - 1 - left, dp, nck, log2))
    dp[n] = ans
    return ans

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

def getLeft(n, log2):
    if (n == 1):
        return 0
    h = log2[n]
    numh = (1 << h) #(2 ^ h)
    last = n - ((1 << h) - 1) # (2^h - 1)
 
    if (last >= (numh // 2)):
        return (1 << h) - 1 # (2^h) - 1
    else:
        return (1 << h) - 1 - ((numh // 2) - last)

# Return 2
print(Solution(3))
# Return 3
print(Solution(4))
# Return 3360
print(Solution(10))