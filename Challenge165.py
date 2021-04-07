"""
Given an array of integers, return a new array where each element
in the new array is the number of smaller elements to the right
of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0]
"""

# Solution 1, runs in O(n^2) time and O(n) space
def Solution1(in1):
    l = len(in1)
    retVal = [0] * l

    for i in range(0, l):
        for j in range(i+1, l):
            if in1[i] > in1[j]:
                retVal[i] += 1

    return retVal

in1 = [3, 4, 9, 6, 1]
print(Solution1(in1))