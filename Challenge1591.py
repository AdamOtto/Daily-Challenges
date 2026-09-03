"""
Given a list of integers S and a target number k, write a
function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list.
You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24,
return [12, 9, 2, 1] since it sums up to 24.
"""

def Solution(ar, k):
    temp1 = sorted(ar, reverse = True)
    temp2 = k
    retVal = []
    
    for i in range(len(temp1)):
        if temp1[i] > 0 and temp1[i] <= temp2:
            temp2 -= temp1[i]
            retVal.append(temp1[i])
    
    if sum(retVal) == k:
        return retVal
    return None

# Return [12, 9, 2, 1]
print(Solution([12, 1, 61, 5, 9, 2], 24))

# Return [8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 2]
print(Solution([5,3,1,5,7,2,4,561,5,3,6,2,99,5,8,2,7,5,3,7,0,0,2,6,3,6,6,7,2,4,2,1], 87))