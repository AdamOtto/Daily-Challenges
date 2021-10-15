"""
Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:

Given N = 4, return 1 (4)
Given N = 17, return 2 (16 + 1)
Given N = 18, return 2 (9 + 9)
"""

def Solution(N):
    retVal = N
    i = 1
    while i ** 2 <= N:
        retVal = min(retVal, Helper(N - (i**2)) + 1)
        i += 1
    return retVal

def Helper(N):
    if N == 0:
        return 0
    if N < 0:
        return -1
    
    for i in reversed(range(1, N + 1)):
        temp = Helper(N - (i**2))
        if temp >= 0:
            return temp + 1
    return -1

print(Solution(4))
print(Solution(17))
print(Solution(18))
print(Solution(100))
print(Solution(2058))