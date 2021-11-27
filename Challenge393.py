"""
Given an array of integers, return the largest range,
inclusive, of integers that are all included in the array.

For example, given the array [9, 6, 1, 3, 8, 10, 12, 11],
return (8, 12) since 8, 9, 10, 11, and 12 are all in the array.
"""

# O(nlogn)
def Solution(ar):
    ar = sorted(ar)
    start = 0
    end = 1
    retVal = None
    while end < len(ar):
        temp = ar[start:end + 1]
        if len(temp) == temp[-1] - temp[0] + 1:
            if retVal is None:
                retVal = (start, end)
            else:
                if temp[-1] - temp[0] > retVal[1] - retVal[0]:
                    retVal = (start, end)
        else:
            start = end
        end += 1
    return (ar[retVal[0]], ar[retVal[1]])

# Return (8, 12)
print(Solution([9, 6, 1, 3, 8, 10, 12, 11]))

# return (1, 3)
print(Solution([1,7,30,5,2,11,9,13,3,15,17,19,25,22,20,29]))