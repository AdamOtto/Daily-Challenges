"""
Given an array of numbers N and an integer k, your task is to split N into k partitions
such that the maximum sum of any partition is minimized. Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8,
since the optimal partition is [5, 1, 2], [7], [3, 4] or [5, 2], [7, 1], [3, 4].
"""
import sys

# O(Nlog(N))
def Solution(N, k):
    partitions = [ []for i in range(k) ]
    N.sort(reverse=True)

    for i in range(len(N)):
        ind = 0
        size = sys.maxsize
        for j in range(k):
            if sum(partitions[j]) == 0:
                ind = j
                break
            elif sum(partitions[j]) < size:
                size = sum(partitions[j])
                ind = j
        partitions[ind].append(N[i])
    #print(partitions)
    retVal = 0
    for i in range(k):
        if sum(partitions[i]) > retVal:
            retVal = sum(partitions[i])
    return retVal


N = [5, 1, 2, 7, 3, 4]
k = 3
print(Solution(N, k))

N = [22, 31, 24, 68, 42, 61, 45, 12, 1, 23, 12, 901, 132, 743, 105, 540, 298, 6]
k = 3
print(Solution(N, k))