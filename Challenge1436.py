"""
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1],
return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""
def Solution(ar):
    start = 0
    end = 1
    retVal = 0
    l = len(ar)
    
    while start < l:
        #print("Checking", ar[start:end])
        if CheckUniq(ar[start:end]):
            retVal = max(retVal, abs(end - start))
            if end >= l:
                start = min(start + 1, l + 1)
            else:
                end = min(end + 1, l + 1)
        else:
            start = min(start + 1, l + 1)
    return retVal


def CheckUniq(ar):
    d = set()
    for i in range(len(ar)):
        d.add(ar[i])
    return len(d) == len(ar)

# Return 5
print(Solution([5, 1, 3, 5, 2, 3, 4, 1]))

# Return 7
print(Solution([1, 2, 3, 4, 5, 6, 7]))

# Return 1
print(Solution([1, 1, 1, 1, 1, 1, 1]))