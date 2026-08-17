"""
Given an array of numbers of length N, find both the
minimum and maximum using less than 2 * (N - 2) comparisons.
"""
import sys

def Solution(ar):
    l = len(ar)
    if l == 0:
        return (None, None)
    if l == 1:
        return (None, ar[0])
    
    minAr = ar[0]
    maxAr = ar[1]

    if minAr > maxAr:
        minAr = ar[1]
        maxAr = ar[0]

    for i in range(2, l):
        if ar[i] > maxAr:
            maxAr = ar[i]
        if ar[i] < minAr:
            minAr = ar[i]
    return minAr, maxAr

# Return 1, 5
print(Solution([1,2,3,4,5]))

# Return 1, 100
print(Solution([1,1,1,20,1,10,1,1,100,1,1,30,1,40,1,1,50,1,1,1,70,60,1,90,1,80,1,1,1]))