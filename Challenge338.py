"""
Given an integer n, find the next biggest integer with the same number of 1-bits on.
For example, given the number 6 (0110 in binary), return 9 (1001).
"""

def Solution1(N):
    ones = get1s(N)
    nextFound = False
    temp = N
    while not nextFound:
        temp += 1
        if get1s(temp) == ones:
            nextFound = True
    return temp


def get1s(N):
    temp = N
    oneCount = 0
    while temp > 0:
        if temp & 1 == 1:
            oneCount += 1
        temp >>= 1
    return oneCount

def Solution2(N):
    next = 0
    if N:
        right = N & (-N)
        nextHighest = N + int(right)
        right1Pattern = N ^ nextHighest
        right1Pattern = int(right1Pattern) / int(right)
        right1Pattern = int(right1Pattern) >> 2
        next = nextHighest | right1Pattern
    return next

# Return 6
print(Solution1(6))
print(Solution2(6))

# Return 1151
print(Solution1(1020))
print(Solution2(1020))

# Return 1316
print(Solution1(1314))
print(Solution2(1314))
    