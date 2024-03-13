"""
Given an array and a number k that's smaller than the length of the array,
rotate the array to the right k elements in-place.
"""

def Solution(ar, k):
    for i in range(k):
        temp = ar[0]
        for j in range(1, len(ar)):
            ar[j - 1] = ar[j]
        ar[len(ar) - 1] = temp
    return ar


# Return [4, 5, 1, 2, 3]
print(Solution([1,2,3,4,5], 3))

# Return ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(Solution(['g','a', 'b', 'c', 'd', 'e', 'f'], 1))