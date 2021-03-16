"""
Given an array of integers in which two elements appear exactly
once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""

def Solution(arr):
    l = len(arr)

    xorSum = arr[0]

    for i in range(1, l):
        xorSum = xorSum ^ arr[i]

    xorSum = (xorSum & ~(xorSum - 1))

    sum1 = 0
    sum2 = 0

    for i in range(0,l):
        if xorSum & arr[i] > 0:
            sum1 = (sum1 ^ arr[i])
        else:
            sum2 = (sum2 ^ arr[i])

    print(sum1)
    print(sum2)


in1 = [2, 11, 6, 9, 10, 2, 6, 10]
Solution(in1)