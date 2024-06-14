"""
Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array
in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""
import heapq as h

def Solution(ar, k):
    for i in range(k, len(ar) + 1):
        print(str(findMax(ar[i - k:i])))


def findMax(ar):
    heap = []
    h.heapify(heap)
    for i in ar:
        h.heappush(heap, -1 * i)
    return -1 * h.heappop(heap)

# Return 10, 7, 8, 8
Solution([10,5,2,7,8,7], 3)

print()

# Return 9, 10, 11, ..., 98, 99, 100
in1 = range(0, 100 + 1)
Solution(in1,10)