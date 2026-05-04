"""
Given an array of integers, find the maximum XOR of any two elements.
"""
def Solution(ar):
    retVal = -1
    l = len(ar)
    for i in range(l):
        for j in range(i + 1, l):
            retVal = max(ar[i] ^ ar[j], retVal)
    return retVal

# Return 7
print(Solution([1 ,2 ,3 ,4, 5]))

# Return 3072
print(Solution([1, 2, 4, 8, 16, 32,64, 128, 256, 512, 1024, 2048]))