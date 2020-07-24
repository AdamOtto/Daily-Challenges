"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

in1 = list(range(-1000, 1000030 + 1))
in1.remove(73384)

"""#Solution 1:  If input was hashable array, this would be a better answer.
t = 1
while t in in1:
    t += 1
print(t)
"""

def findMissingNumber(inp):
    m = max(inp)
    if m < 1:
        return 1
    if len(inp) == 1:
        return m+1
    
    l = [0]*m
    for x in inp: #n
        if x > 0:
            l[x-1] = x
    if 0 in l: #n
        return l.index(0) + 1
    else:
        return m + 1
    #O(2n) = O(n)
    #Constant space: n + r, where r <= n
    
print(findMissingNumber(in1))