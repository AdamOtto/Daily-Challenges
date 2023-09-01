"""
Given a list of elements, find the majority element,
which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""
import math

def Solution(ar):
    l = len(ar)
    retVal = 0
    d = {}
    for i in range(l):
        if ar[i] not in d:
            d[ar[i]] = 0
        d[ar[i]] += 1
    
    for key, val in d.items():
        if val >= math.floor(l / 2.0):
            retVal = max(retVal, key)
    return retVal

# Return 1
print(Solution([1, 2, 1, 1, 3, 4, 0]))
# Return 2
print(Solution([2,4,2,1,2,4,5,2,2,5,2,3,2,1,5,2,5,3,2,3,3,2,4,1,2,4,2,4,2,2,4,2,2,1,2,2,2,2,1,4]))