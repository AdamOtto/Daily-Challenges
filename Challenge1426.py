"""
Given an array of integers,
find the maximum XOR of any two elements
"""
def Solution(ar):
    l = len(ar)
    retVal = None
    for i in range(l):
        for j in range(i + 1, l):
            if retVal is None:
                retVal = ar[i] ^ ar[j]
            else:
                retVal = max(retVal, ar[i] ^ ar[j])
    return retVal

# Return 7
print(Solution([1,2,3,4,5,6]))

# Return 3840
print(Solution([3, 12, 48, 192, 768, 3072]))