"""
Given an array and a number k that's smaller than the length of the array,
rotate the array to the right k elements in-place.
"""
def Solution(ar, k):
    for i in range(k): ar.insert(0, ar.pop())
    return ar

# Return [4, 5, 6, 1, 2, 3]
print(Solution([1,2,3,4,5,6], 3))