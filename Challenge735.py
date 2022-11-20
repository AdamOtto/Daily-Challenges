"""
Given an unsorted array, in which all elements are
distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both
its left and right neighbors. It is guaranteed that the
first and last elements are lower than all others.
"""
def Solution(ar, low = None, high = None):
    l = len(ar)
    if low is None:
        low = 0
    if high is None:
        high = l - 1
    mid = int((low + high)/2)
    
    if ((mid == 0 or ar[mid - 1] <= ar[mid]) and (mid == l - 1 or ar[mid + 1] <= ar[mid])):
        return mid
    
    elif (mid > 0 and ar[mid - 1] > ar[mid]):
        return Solution(ar, low, (mid - 1))
    else:
        return Solution(ar, (mid + 1), high)
    
# Return 2
print(Solution([2,5,72,4,7,8,5]))

# Return 6
print(Solution([1,2,3,4,5,6,7]))

# Return 1
print(Solution([1,2,1,2,1,2,1,2,1]))