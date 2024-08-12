"""
Given an array of numbers N and an integer k,
your task is to split N into k partitions such that
the maximum sum of any partition is minimized.
Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since the optimal partition is [5, 2, 1], [7], [3, 4] or [5, 2], [7, 1], [3, 4].
"""
def Solution(ar, k):
    maxSum = sum(ar)
    l = len(ar)
    partitions = []
    for i in range(k):
        partitions.append([])
    
    ar = sorted(ar, reverse = True)
    
    for i in range(l):
        ind = 0
        curSum = maxSum
        for j in range(k):
            if sum(partitions[j]) < curSum:
                ind = j
                curSum = sum(partitions[j])
        partitions[ind].append(ar[i])
    
    retVal = 0
    for i in range(k):
        retVal = max(retVal, sum(partitions[i]))
    return retVal

# Return 8
print(Solution([5, 1, 2, 7, 3, 4], 3))

# Return 11
print(Solution([1,2,3,4,5,6,7,8,9,10], 5))

# Return 102
print(Solution([2, 5, 100, 97], 2))