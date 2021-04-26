"""
Given an array of elements, return the length of the
longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1],
return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""
# O(n)
def Solution(ar):
    l = len(ar)
    d = {}
    index = 0
    retVal = []
    for i in range(0, l):
        if ar[i] not in d:
            d[ar[i]] = i
        else:
            temp = ar[index:i]
            d = {}
            d[ar[i]] = i
            index = i
            if len(temp) > len(retVal):
                retVal = temp

    if len(d) > len(retVal):
        retVal = ar[index:l]

    return retVal



in1 = [5, 1, 3, 5, 2, 3, 4, 1]
print(Solution(in1))