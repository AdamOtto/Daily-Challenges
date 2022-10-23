"""
A fixed point in an array is an element whose value is equal to its index.
Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2.
Given [1, 5, 7, 8], you should return False.
"""
def Solution(ar):
    l = len(ar)
    for i in range(l):
        if i == ar[i]:
            return i
    return None

# Return 2
print(Solution([-6, 0, 2, 40]))

# Return None
print(Solution([1, 5, 7, 8]))