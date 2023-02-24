"""
Given an array of elements, return the length of the
longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1],
return 5 as the longest subarray of
distinct elements is [5, 2, 3, 4, 1].
"""

# O(n)
def Solution(ar):
    ind = {}
    for a in ar:
        ind[a] = 0
    j = 0
    retVal = 0
    
    for i in range(len(ar)):
        j = max(ind[ar[i]], j)
        retVal = max(retVal, i - j + 1)
        ind[ar[i]] = i + 1
    return retVal


# Return 5
in1 = [5, 1, 3, 5, 2, 3, 4, 1]
print(Solution(in1))

# Return 5
in1 = [5, 1, 3, 5, 2, 4]
print(Solution(in1))

# Return 2
in1 = [5,5,2,5,5,5]
print(Solution(in1))