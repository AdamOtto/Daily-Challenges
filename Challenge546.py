"""
Given an array of integers, return a new array where each element
in the new array is the number of smaller elements to the right
of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1],
return [1, 1, 2, 1, 0]
"""

def Solution(ar):
    l = len(ar)
    retVal = [0] * l
    
    for i in range(l):
        for j in range(i + 1, l):
            if ar[j] < ar[i]:
                retVal[i] += 1
    return retVal



print(Solution([3,4,9,6,1]))