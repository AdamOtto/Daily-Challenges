"""
Given an array of integers where every integer occurs
three times except for one integer, which only occurs once,
find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6],
return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""

def Solution(ar):
    l = len(ar)
    ones = 0
    twos = 0
    for i in range(l):
        twos = twos ^ (ones & ar[i])
        ones = ones ^ ar[i]
        commonBits = ~(twos & ones)
        ones &= commonBits
        twos &= commonBits
    return ones

# Return 1
print(Solution([6, 1, 3, 3, 3, 6, 6]))

# Return 7
print(Solution([1,2,3,1,2,3,1,2,3,4,5,6,4,5,6,4,5,6,7,8,9,8,9,8,9]))