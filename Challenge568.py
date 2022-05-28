"""
Given a sorted list of integers,
square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""

# O(nlogn).  Input doesn't need to be sorted.
def Solution(ar):
    retVal = []
    for i in range(len(ar)):
        insert(retVal, ar[i]**2)
    return retVal

def insert(ar, val):
    if len(ar) == 0:
        ar.append(val)
        return
    elif len(ar) == 1:
        if ar[0] > val:
            ar.insert(0, val)
        else:
            ar.append(val)
        return
    high = len(ar) - 1
    low = 0
    mid = int((high - low) / 2) + low
    
    while low < high:
        if val <= ar[mid]:
            if mid == 0:
                ar.insert(mid, val)
                return
            elif val >= ar[mid - 1]:
                ar.insert(mid, val)
                return
        if val > ar[mid]:
            if low == mid:
                low = mid + 1
            else:
                low = mid
        else:
            if high == mid:
                high = mid - 1
            else:
                high = mid
        mid = int((high - low) / 2) + low
    if mid == 0:
        ar.insert(mid, val)
    if mid == len(ar) - 1:
        if ar[len(ar) - 1] > val:
            ar.insert(len(ar) - 1, val)
        else:
            ar.append(val)
    return

# Return [0, 4, 4, 9, 81]
print(Solution([-9, -2, 0, 2, 3]))

# Return [1, 4, 9, 16]
print(Solution([1,2,3,4]))

# Return [9, 16, 36, 361, 400, 10000, 16900]
print(Solution([-100,-20,-4,3,6,19,130]))

# Return [1, 4, 9, 16, 25]
print(Solution([5,4,3,2,1]))

# Return [1, 4, 9, 16, 64, 100]
print(Solution([10,-1,3,4,-2,8]))