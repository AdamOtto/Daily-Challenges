"""
Given an integer n, find the next biggest integer with the same number of 1-bits on.
For example, given the number 6 (0110 in binary), return 9 (1001).
"""
def Solution(N):
    next = 0
    if N:
        right = N & (-N)
        nextHighest = N + int(right)
        right1Pattern = N ^ nextHighest
        right1Pattern = int(right1Pattern) / int(right)
        right1Pattern = int(right1Pattern) >> 2
        next = nextHighest | right1Pattern
    return next

# Return 9
print(Solution(6))

# Return 2
print(Solution(1))

# Return 104
print(Solution(100))

# Return 16
print(Solution(8))