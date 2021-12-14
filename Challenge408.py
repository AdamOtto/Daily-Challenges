"""
Given an array of numbers representing the stock prices of a company
in chronological order and an integer k, return the maximum profit you can
make from k buys and sells. You must buy the stock before you can sell it,
and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1],
you should return 3.
"""

def Solution(ar, k):
    retVal = 0
    temp = ar.copy() 
    for i in range(k):
        localMin = findLocalMin(temp)
        if localMin < len(temp):
            localMax = findLocalMax(temp, localMin)
            retVal += temp.pop(localMax) - temp.pop(localMin)
    return retVal

def findLocalMin(ar):
    l = len(ar)
    for i in range(0,l - 1):
        if ar[i] < ar[i+1]:
            return i
    return l

def findLocalMax(ar, localMin):
    retVal = len(ar)
    maxVal = ar[localMin]
    for i in range(localMin, len(ar)):
        if maxVal < ar[i]:
            maxVal = ar[i]
            retVal = i
    return retVal
    
# Return 3
in1 = [5, 2, 4, 0, 1]
k = 2
print(Solution(in1, k))

# Return 100
in1 = [5, 0, 1, 40, 100]
k = 1
print(Solution(in1, k))

# Return 0
in1 = [5, 4, 3, 2, 1]
k = 1
print(Solution(in1, k))