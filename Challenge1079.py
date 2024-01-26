"""
Given an array of integers in which two elements appear exactly
once and all other elements appear exactly twice,
find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10],
return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""
# O(n) time and O(1) space
def Solution(ar):
    l = len(ar)
    xor = 0
    for i in range(l):
        xor = xor ^ ar[i]
    xor = xor & -xor
    val1 = val2 = 0
    for i in range(l):
        if xor & ar[i]:
            val1 = val1 ^ ar[i]
        else:
            val2 = val2 ^ ar[i]
    
    return val1, val2


print(Solution([2, 4, 6, 8, 10, 2, 6, 10]))