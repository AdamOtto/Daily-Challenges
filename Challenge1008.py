"""
Given an array of integers,
find the maximum XOR of any two elements.
"""
def Solution(ar):
    l = len(ar)
    retVal = 0
    mask = 0
    
    d = set()
    
    for i in range(30,-1,-1):
        mask |= (1 << i)
        temp = retVal | (1 << i)
    
        for i in range(l):
            d.add(ar[i] & mask)
        
        for val in d:
            if temp ^ val in d:
                retVal = temp
                break
        
        d = set()
    return retVal

# Return 7
print(Solution([1,2,3,4,5]))
# Return 31
print(Solution([10,11,12,13,14,15,16]))