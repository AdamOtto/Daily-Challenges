"""
Let's define a "sevenish" number to be one which is either a power of 7,
or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49,
and so on. Create an algorithm to find the nth sevenish number.
"""

def Solution(n):
    i = 0
    retVal = 0
    while n > 0:
        if n & 1 == 1:
            retVal += pow(7, i)
        i += 1
        n >>= 1
    return retVal

# Return 1
print(Solution(1))
# Return 7
print(Solution(2))
# Return 8
print(Solution(3))
# Return 49
print(Solution(4))
# Return 50
print(Solution(5))