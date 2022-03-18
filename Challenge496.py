"""
Write an algorithm that finds the total number
of set bits in all integers between 1 and N.
"""

def Solution(ar):
    if ar <= 0:
        return 0
    temp = ar
    retVal = 0
    while temp > 0:
        if temp & 1 == 1:
            retVal += 1
        temp >>= 1
    return retVal

# Return 1
print(Solution(4))
print(Solution(8))
print(Solution(16))

# Return 2
print(Solution(5))
print(Solution(9))
print(Solution(17))

# Return 3
print(Solution(7))
print(Solution(11))
print(Solution(19))

# Return 4
print(Solution(15))
