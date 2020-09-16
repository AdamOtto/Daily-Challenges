'''
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time.
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
'''

def Solution(in1, n, k):
    p = findPivotPoint(in1, 0, n)
    
    if in1[p] == k: 
        return pivot 
    if in1[0] <= k: 
        return binarySearch(in1, 0, p-1, k); 
    return binarySearch(in1, p + 1, n-1, k);
    

def findPivotPoint(arr, low, high):
    if high < low: 
        return -1
    if high == low: 
        return low
    mid = int((low + high) / 2)
    if mid < high and arr[mid] > arr[mid + 1]: 
        return mid 
    if mid > low and arr[mid] < arr[mid - 1]: 
        return (mid-1) 
    if arr[low] >= arr[mid]: 
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid + 1, high)

def binarySearch(arr, low, high, key): 
    if high < low: 
        return -1
    mid = int((low + high)/2) 
    if key == arr[mid]: 
        return mid 
    if key > arr[mid]: 
        return binarySearch(arr, mid + 1, high, key); 
    return binarySearch(arr, low, mid -1, key); 

in1 = [13, 18, 25, 2, 8, 10]
k = 8
t = Solution(in1, len(in1), k)
print(t)