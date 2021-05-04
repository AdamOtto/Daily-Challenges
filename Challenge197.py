"""
Given an array and a number k that's smaller than the length of the array,
rotate the array to the right k elements in-place.
"""

def Rotate(ar, val):
    l = len(ar)
    for i in range(1, l):
        ar[i - 1] = ar[i]
    ar[l - 1] = val
    return


def Solution(ar, k):
    for i in range(0, k):
        temp = ar[0]
        Rotate(ar, temp)
    return

in1 = [1,2,3,4,5,6,7]
k = 2
Solution(in1, k)
print(in1)