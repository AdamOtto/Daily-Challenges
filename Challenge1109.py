"""
Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
"""

def Solution(ar, x):
    low = []
    mid = []
    high = []
    
    for i in range(len(ar)):
        if ar[i] < x:
            low.append(ar[i])
        elif ar[i] == x:
            mid.append(ar[i])
        else:
            high.append(ar[i])
    
    return low + mid + high


# Return [9, 3, 5, 10, 10, 12, 14]
print(Solution([9, 12, 3, 5, 14, 10, 10], 10))

# Return [1, 2, 3, 4, 5, 6, 7]
print(Solution([1, 5, 4, 2, 6, 3, 7], 4))