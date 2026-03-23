"""
Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
"""
def Solution(lst, x):
    low = []
    mid = []
    high = []
    
    for l in lst:
        if l < x:
            low.append(l)
        elif l == x:
            mid.append(l)
        elif l > x:
            high.append(l)
    return [*low, *mid, *high]

# Return [9, 3, 5, 10, 10, 12, 14]
print(Solution([9, 12, 3, 5, 14, 10, 10], 10))

# Return [5, 4, 3, 2, 1, 6, 10, 9, 8, 7]
print(Solution([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 6))