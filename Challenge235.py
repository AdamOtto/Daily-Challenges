"""
Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.
"""
import sys

# method 1, O(1) space and O(N) time
def Solution1(ar):
    #Assumes len(ar) >= 2
    minAr = ar[0]
    maxAr = ar[1]

    if minAr > maxAr:
        minAr = ar[1]
        maxAr = ar[0]

    for i in range(2, len(ar)):
        if ar[i] > maxAr:
            maxAr = ar[i]
        if ar[i] < minAr:
            minAr = ar[i]
    return minAr, maxAr

# Method 2
def Solution2(ar):
    maxAr = 0
    minAr = 0
    i = 0
    if ar[0] % 2 == 0:
        maxAr = max(ar[0], ar[1])
        minAr = min(ar[0], ar[1])
        i = 2
    else:
        maxAr = minAr = ar[0]
        i = 1

    while i < len(ar) - 1:
        if ar[i] < ar[i + 1]:
            maxAr = max(maxAr, ar[i + 1])
            minAr = min(minAr, ar[i])
        else:
            maxAr = max(maxAr, ar[i])
            minAr = min(minAr, ar[i + 1])
        i += 2
    return minAr, maxAr

in1 = [1,2,-2,3,4,5,6,7,500]
print(Solution1(in1))
print(Solution2(in1))