"""
Given an array of numbers, find the maximum
sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86],
the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0,
since we would not take any elements.

Do this in O(N) time.
"""

def Solution(ar):
    l = len(ar)
    last = ar[0]
    t = 0
    for i in range(1, l):
        t1 = ar[i]
        t2 = ar[i] + last
        last = max(t1, t2)
        if last > t:
            t = last
    if t > 0:
        return t
    return 0

# Return 137
print(Solution([34, -50, 42, 14, -5, 86]))
# Return 0
print(Solution([-5, -1, -8, -9]))
# Return 50
print(Solution([0,1,0,-1,0,0,2,0,-11,50]))