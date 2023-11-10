"""
A sorted array of integers was
rotated an unknown number of times.

Given such an array, find the index of the element
in the array in faster than linear time.
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8,
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""

def Solution(ar, k):
    n = len(ar)
    p = findPivotPoint(ar, 0, n)
    
    if ar[p] == k: 
        return p 
    if ar[0] <= k: 
        return binarySearch(ar, 0, p-1, k); 
    return binarySearch(ar, p + 1, n-1, k);
    

def findPivotPoint(arr, low, high):
    if high < low: 
        return -1
    if high == low: 
        return low
    mid = int((low + high) / 2)
    if mid < high and arr[mid] > arr[min(len(arr) - 1, mid + 1)]: 
        return mid 
    if mid > low and arr[mid] < arr[max(0, mid - 1)]: 
        return (mid-1) 
    if arr[low] >= arr[mid]: 
        return findPivotPoint(arr, low, mid-1)
    return findPivotPoint(arr, mid + 1, high)

def binarySearch(arr, low, high, key): 
    if high < low: 
        return -1
    mid = int((low + high)/2) 
    if key == arr[mid]: 
        return mid 
    if key > arr[mid]: 
        return binarySearch(arr, mid + 1, high, key); 
    return binarySearch(arr, low, mid -1, key);
    
# Return 3
print(Solution([5,6,7,1,2,3,4], 1))

# Return 4
print(Solution([13, 18, 25, 2, 8, 10], 8))

# Return 6
print(Solution([2,3,4,5,6,7,8,1], 8))