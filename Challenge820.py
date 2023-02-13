"""
Given an array of integers, find the first missing positive integer
in linear time and constant space. In other words, find the lowest
positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
# O(n)
def Solution(ar):
    m = max(ar)
    if m < 1:
        return 1
    if len(ar) == 1:
        return m+1
    
    l = [0]*m
    for x in ar:
        if x > 0:
            l[x-1] = x
    if 0 in l:
        return l.index(0) + 1
    else:
        return m + 1

# Return 2
print(Solution([3, 4, -1, 1]))

# Return 3
print(Solution([1, 2, 0]))

# Return 743
in1 = [i for i in range(1000)]
in1.pop(743)
print(Solution(in1))