"""
Given an array of integers, return a new array where each element in the new
array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""
def Solution(ar):
    retVal = []
    for i in range(len(ar)):
        temp = 0
        for j in range(i + 1, len(ar)):
            if ar[j] < ar[i]:
                temp += 1
        retVal.append(temp)
    return retVal

# Return [1, 1, 2, 1, 0]
print(Solution([3, 4, 9, 6, 1]))

# Return [0, 2, 1, 1, 0]
print(Solution([4,8,6,8,4]))