"""
Write an algorithm that finds the total number of
set bits in all integers between 1 and N.
"""

def Solution(N):
    retVal = 0
    
    for i in range(1, N + 1):
        temp = i
        while temp > 0:
            if temp & 1 == 1:
                retVal += 1
            temp >>= 1
    return retVal

print(Solution(3))
print(Solution(6))
print(Solution(7))