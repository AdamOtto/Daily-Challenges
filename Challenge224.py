"""
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

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



in1 = [1,2,3,10]
print(Solution(in1))
in1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31]
print(Solution(in1))