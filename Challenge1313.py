"""
Write a function that returns the bitwise AND of all integers between M and N, inclusive.
"""
# O(n), where n is number of bits in N and M.
def Solution(M, N):
    if M > N:
        temp = M
        M = N
        N = temp
    
    sigDigM = GetMostSigDig(M)
    sigDigN = GetMostSigDig(N)
    retVal = 0
    
    while sigDigM == sigDigN and sigDigN > 0:
        retVal += sigDigN
        M -= sigDigM
        N -= sigDigN
        sigDigM = GetMostSigDig(M)
        sigDigN = GetMostSigDig(N)
    
    return retVal

def GetMostSigDig(num):
    i = 0
    if num <= 0:
        return 0
    while num != 1:
        num >>= 1
        i += 1
    num <<= i
    return num
    
# Return 12
print(Solution(12, 15))

# Return 8
print(Solution(9, 8))

# Return 0
print(Solution(9, 25))

# Return 255
print(Solution(255, 255))