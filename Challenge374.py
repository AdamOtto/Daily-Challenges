"""
Given a sorted array arr of distinct integers,
return the lowest index i for which arr[i] == i. Return null if there is no such index.

For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2.
Even though arr[3] == 3, we return 2 since it's the lowest index.
"""
import math

# O(n) Solution
def Solution1(ar):
    l = len(ar)
    
    for i in range(l):
        if ar[i] == i:
            return i
    return None

# O(logn)
def Solution2(ar):
    l = len(ar)
    low = 0
    high = l - 1
    mid = int(math.ceil((low + high) / 2))
    
    while low <= high and high != mid and low != mid:
        if ar[mid] == mid:
            return mid
        if ar[mid] < mid:
            high = mid
            mid = int(math.ceil((low + high) / 2))
        else:
            low = mid
            mid = int(math.ceil((low + high) / 2))
    
    if ar[high] == high:
        return high
    elif ar[low] == low:
        return low
    
    return None


print(Solution1([-5, -3, 2, 3]))
print(Solution2([-5, -3, 2, 3]))

# Return 97
in1 = []
for i in range(0, 99):
    in1.append(i + 1)
in1[97] = 97
print(Solution1(in1))
print(Solution2(in1))

# Return None
in1 = []
for i in range(0, 99):
    in1.append(i + 1)
print(Solution1(in1))
print(Solution2(in1))