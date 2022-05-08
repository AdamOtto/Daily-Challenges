"""
Given an array of integers,
find the maximum XOR of any two elements.
"""

def Solution(ar):
    l = len(ar)
    retVal = 0
    
    for i in range(l):
        for j in range(i + 1, l):
            if ar[i] ^ ar[j] > retVal:
                retVal = ar[i] ^ ar[j]
    return retVal
    
# Return 7
print(Solution([1,2,3,4,5,6]))

# Return 506
print(Solution([101,3,301,241,59,23,415,32,15,20]))