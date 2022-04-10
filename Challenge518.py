"""
Given an array of numbers and a number k, determine if there are
three entries in the array which add up to the specified number k.

For example, given [20, 303, 3, 4, 25] and k = 49,
return true as 20 + 4 + 25 = 49.
"""

def Solution(ar, k):
    retVal = []
    l = len(ar)
    temp = sorted(ar, reverse=True)
    for i in range(l):
        if len(retVal) < 3 and sum(retVal) + temp[i] <= k:
            retVal.append(temp[i])
        elif len(retVal) == 3:
            test = sum(retVal[1:])
            if sum(retVal[1:]) + temp[i] <= k:
                retVal.pop(0)
                retVal.append(temp[i])
        
        if sum(retVal) == k:
            break
    if sum(retVal) == k:
        return retVal
    else:
        return None
    
# Return [25, 20, 4]
print(Solution([20,303,3,4,25], 49))

# Return None
print(Solution([1,2,4,16,8], 49))

# Return [16, 8, 1]
print(Solution([1,2,4,16,8], 25))