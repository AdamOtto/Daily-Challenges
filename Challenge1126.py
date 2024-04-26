"""
Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:

Given N = 4, return 1 (4)
Given N = 17, return 2 (16 + 1)
Given N = 18, return 2 (9 + 9)
"""
import math
def Solution(N):
    top = 0
    divs = []
    for i in range(1, N):
        if math.pow(i,2) <= N:
            top  = i
        if N % int(math.pow(i,2)) == 0:
            divs.append( int(math.pow(i,2)) )
    retval = []
    val = N
    while val > 0:
        if math.pow(top,2) <= val:
            val -= math.pow(top,2)
            retval.append(int(math.pow(top,2)))
        if val == 0:
            break
        if math.pow(top,2) > val:
            top -= 1
    
    for i in divs:
        if N / i < len(retval):
            return " + ".join(map(str,([i] * int(N / i) )))
    return " + ".join(map(str,retval))

# Return 4
print(Solution(4))

# Return 16 + 1
print(Solution(17))

# Return 9 + 9
print(Solution(18))

# Return 16 + 16 + 16
print(Solution(48))

# Return 49 + 1
print(Solution(50))