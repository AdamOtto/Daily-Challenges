"""
Given an array of numbers and an index i,
return the index of the nearest larger number of the number at index i,
where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0,
you should return 3.

If two distances to larger numbers are the equal,
then return any one of them.
If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""

def Solution(n, i):
    l = len(n)
    iDown = max(0, i - 1)
    iUp = min(l - 1, i + 1)
    while iDown != 0 or iUp != l:
        if n[iDown] > n[i]:
            return abs(iDown - i)
        if n[iUp] > n[i]:
            return abs(iUp - i)
        iDown = max(0, iDown - 1)
        iUp = min(l - 1, iUp + 1)
    return None
    
# Return 3
print(Solution([4, 1, 3, 5, 6], 0))

# Return 1
print(Solution([5,4,3,2,1], 1))

# Return 4
print(Solution([101,0,1,0,100], 4))