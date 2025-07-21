"""
Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2],
the longest consecutive element sequence is [1, 2, 3, 4].
Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

def Solution(ar):
    l = len(ar)
    s = set()
    retVal = 0
    for a in ar:
        s.add(a)
    
    for i in range(l):
        if ar[i] - 1 not in s:
            temp = ar[i]
            while temp in s:
                temp += 1
            retVal = max(retVal, temp - ar[i])
    return retVal

# Return 4
print(Solution([100, 4, 200, 1, 3, 2]))
# Return 9
print(Solution([1,6,4,2,3,5,9,7,8]))
# Return 1
print(Solution([1,3,5,7,9,11,13,15,17,19]))
# Return 5
print(Solution([3,2,1,9,100,8,101,7,103,104,102,6]))