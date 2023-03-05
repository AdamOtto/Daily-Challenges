"""
Given integers M and N, write a program that counts how many
positive integer pairs (a, b) satisfy the following conditions:

a + b = M
a XOR b = N
"""
def Solution(M, N):
    retVal = 0
    for a in range(int(M / 2) + 1):
        b = M - a
        if a ^ b == N:
            retVal += 1
    return retVal

# Return 4
print(Solution(100, 100))
# Return 1
print(Solution(10, 2))