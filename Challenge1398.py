"""
Given an array of integers, write a function to determine whether the array
could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true,
since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false,
since we can't modify any one element to get a non-decreasing array.
"""

def Solution(ar):
    count = 0
    l = len(ar)
    if (ar[l - 1] <= ar[l - 2]):
        ar[l-1] = ar[l-2] + 1
        count += 1
    if (ar[0] >= ar[1]):
        ar[0] = ar[1] - 1
        count += 1
    
    for i in range(1, l - 1):
        if ar[i] > ar[i - 1] and ar[i] > ar[i + 1]:
            ar[i] = (ar[i - 1] + ar[i + 1]) // 2
            if (ar[i] == ar[i - 1] or ar[i] == ar[i + 1]):
                return False
            count += 1
        elif ar[i] < ar[i - 1] and ar[i] < ar[i + 1]:
            ar[i] = (ar[i - 1] + ar[i + 1]) // 2
            if (ar[i] == ar[i - 1] or ar[i] == ar[i + 1]):
                return False
            count += 1
    if count == 1:
        return True
    return False


# Return True
print(Solution([10,5,7]))

# Return False
print(Solution([10,5,1]))

# Return False
print(Solution([1,10,2,3,4,5,6,7,8,9]))

# Return True
print(Solution([1,10,3,4,5,6,7,8,9]))