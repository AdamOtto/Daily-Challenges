"""
Write an algorithm that finds the total number
of set bits in all integers between 1 and N.
"""

def Solution(ar):
    if ar <= 0:
        return 0
    retVal = 0
    for i in range(1,ar + 1):
        temp = i
        while temp > 0:
            if temp & 1 == 1:
                retVal += 1
            temp >>= 1
    return retVal


# Return 1
print(Solution(1))
# Return 2
print(Solution(2))
# Return 4
print(Solution(3))
# Return 5
print(Solution(4))
# Return 319
print(Solution(100))