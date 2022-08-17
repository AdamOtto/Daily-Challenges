"""
Given a sorted array, find the smallest positive integer
that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
"""

def Solution(ar):
    l = len(ar)
    retVal = 1
    for i in range(0, l):
        if ar[i] <= retVal:
            retVal = retVal + ar[i]
        else:
            break
    return retVal

# Return 7
in1 = [1,2,3,10]
print(Solution(in1))

# Return 56
in1 = [1,2,3,4,5,6,7,8,9,10]
print(Solution(in1))

