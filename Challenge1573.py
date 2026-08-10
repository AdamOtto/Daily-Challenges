"""
Given a array that's sorted but rotated at some unknown pivot,
in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors.
It is guaranteed that the first and last elements are lower than all others.
"""

def Solution(ar):
    l = len(ar)
    low = 0
    high = l - 1
    mid = int((low + high) / 2)
    
    while low != high:
        if ar[mid] > ar[mid - 1] and ar[mid] > ar[mid + 1]:
            return ar[mid]
        else:
            if ar[mid] < ar[mid + 1]:
                low = mid
            elif ar[mid - 1] > ar[mid]:
                high = mid
            mid = int((low + high) / 2)
    return False


# Returns 8
in1 = [1,2,3,4,8,7,6,5]
print(Solution(in1))

# Returns 8
in1 = [1,2,3,4,5,6,8,7]
print(Solution(in1))

# Returns 25
in1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,25,24,23,22,21,20,19,18,17,16,15,14]
print(Solution(in1))

# Returns 1000
in1 = []
for i in range(1,250 + 1):
    in1.append(i)
for i in reversed(range(251, 1000 + 1)):
    in1.append(i)
print(Solution(in1))