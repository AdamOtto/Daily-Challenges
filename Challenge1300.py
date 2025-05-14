"""
Given a list of integers and a number K,
return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9,
then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

def Solution(ar, k):
    low = high = 0
    while low <= high:
        if sum(ar[low:high+1]) < k:
            high += 1
        elif sum(ar[low:high+1]) > k:
            low += 1
        else:
            return ar[low:high+1]
    return None

#Return [2,3,4]
print(Solution([1,2,3,4,5], 9))
#Return None
print(Solution([2,2,2,2,2], 1))
#Return [2]
print(Solution([2,2,2,2,2], 2))
# Return [0,1,2,...,49,50]
in1 = [i for i in range(101)]
print(Solution(in1, 1275))