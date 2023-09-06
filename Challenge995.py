"""
Given an array of integers, return a new array such that each
element at index i of the new array is the product of all the
numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
def Solution(ar):
    l = len(ar)
    i = 1
    temp = 1
    
    retVal = [1 for i in range(l)]
    
    for i in range(l):
        retVal[i] = temp
        temp *= ar[i]
    
    temp = 1
    
    for i in range(l - 1, -1, -1):
        retVal[i] *= temp
        temp *= ar[i]
    return retVal

# Return [120, 60, 40, 30, 24]
print(Solution([1,2,3,4,5]))

# Return [2,3,6]
print(Solution([3,2,1]))

# Return [1071645120, 824342400, 765460800, 893037600, 228009600, 369532800, 1190716800, 267911280]
print(Solution([10,13,14,12,47,29,9,40]))