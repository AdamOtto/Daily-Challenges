"""
Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

a + b = M
a XOR b = N
"""

def Solution(M, N):
    a = 0
    b = M
    retVal = []
    for i in range(0, int(M / 2) + 1):
        a = i
        b = M - a
        if a ^ b == N:
            retVal.append( (a,b) )
    return retVal

# Return (1, 3)
print(Solution(4, 2))

# Return (72, 78), (74, 76)
print(Solution(150, 6))