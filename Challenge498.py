"""
Given an array of integers out of order, determine the
bounds of the smallest window that must be sorted in
order for the entire array to be sorted.

For example, given [3, 7, 5, 6, 9],
you should return (1, 3).
"""

# O(n)
def Solution(ar):
    low = high = -1
    l = len(ar)
    # Find low
    for i in range(1, l):
        if ar[i - 1] > ar[i]:
            low = i - 1
            break
    if low == -1:
        return (None, None)
    # Find high
    for i in reversed(range(l - 1)):
        if ar[i + 1] < ar[i]:
            high = i + 1
            break
        if ar[i] < ar[low]:
            high = i
            break
    return (low, high)

# Return (1, 3)
print(Solution([3, 7, 5, 6, 9]))

# Return (None, None)
print(Solution([1,2,3,4,5,6]))

# Return (0, 1)
print(Solution([2,1,3,4,5,6]))

# Return (0, 3)
print(Solution([2,1,4,3,5,6]))