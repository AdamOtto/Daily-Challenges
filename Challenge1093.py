"""
Given an array of integers, return a new array where each element in the new
array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1

Code help from:
https://www.geeksforgeeks.org/count-smaller-elements-on-right-side/
"""
# O(n logn)
def Solution(ar):
    v = []
    l = len(ar)
    
    for i in range(l):
        v.append([ar[i], i])
    
    ans = [0]*l
    
    mergeSort(v, ans, 0, l-1)
    return ans


def mergeSort(v, ans, i, j):
    if i < j:
        mid = (i+j)//2
        mergeSort(v, ans, i, mid)
        mergeSort(v, ans, mid + 1, j)
        merge(v, ans, i, mid, j)


def merge(v, ans, l, mid, h):
    temp = []
    i = l
    j = mid + 1
    
    while (i < mid+1 and j <= h):
        if v[i][0] > v[j][0]:
            ans[v[i][1]] += (h-j+1)
            temp.append(v[i])
            i += 1
        else:
            temp.append(v[j])
            j += 1
    
    while (i <= mid):
        temp.append(v[i])
        i += 1
         
    
    while j <= h:
        temp.append(v[j])
        j += 1
         
    
    k = 0
    i = l
    while (i <= h):
        v[i] = temp[k]
        i += 1
        k += 1

# Return [1, 1, 2, 1, 0]
print(Solution([3, 4, 9, 6, 1]))

# Return [6, 1, 1, 1, 0, 1, 0]
print(Solution([12, 1, 2, 3, 0, 11, 4]))