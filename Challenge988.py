"""
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
"""
import math

def Solution(ar):
    if math.sqrt(ar).is_integer():
        return 1
    
    i = ar
    retVal = []
    
    while i > 0:
        if math.pow(i, 2) > ar:
            i -= 1
            continue
        else:
            ar -= math.pow(i, 2)
            retVal.append(i)
    return len(retVal)

# Return 2
print(Solution(13))

# Return 3
print(Solution(27))

# Return 1
print(Solution(100))