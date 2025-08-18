"""
Given an array of numbers representing the stock prices of a
company in chronological order and an integer k, return the
maximum profit you can make from k buys and sells.
You must buy the stock before you can sell it,
and you must sell the stock before you can buy it again.

For example, given k = 2 and the array
[5, 2, 4, 0, 1], you should return 3.
"""
def Solution(ar, k):
    l = len(ar)
    profit = [[0 for i in range(l + 1)] for j in range(k + 1)]
    for i in range(1, k + 1):
        prevDiff = float('-inf')
        for j in range(1, l):
            prevDiff = max(prevDiff, profit[i - 1][j - 1] - ar[j - 1])
            profit[i][j] = max(profit[i][j - 1], ar[j] + prevDiff)
 
    return profit[k][l - 1]

# Return 3
print(Solution([5, 2, 4, 0, 1], 2))

# Return 0
print(Solution([100,40,30,20,10,5,1,0], 2))

# Return 15
print(Solution([30,29,10,14,16,20,18,19,20,21,15,10,1,3], 3))