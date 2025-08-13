"""
Given an integer n, return the length of the longest
consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""
def Solution(ar):
    count = 0
    retVal = 0
    while ar != 0:
        if ar & 1 == 1:
            count += 1
        else:
            retVal = max(retVal, count)
            count = 0
        ar = ar >> 1
    return max(retVal, count)


# Return 3
print(Solution(156))
# Return 8
print(Solution(255))
# Return 3
print(Solution(11111111))