"""
Given an array of integers and a number k, where 1 <= k <= length of the array.
Compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8]

"""
import heapq as h

def findSubMax(ar, k):
    for i in range(k, len(ar) + 1):
        print(str(findMax(ar[i - k:i])))


def findMax(ar):
    heap = []
    h.heapify(heap)
    for i in ar:
        h.heappush(heap, -1 * i)
    return -1 * h.heappop(heap)


#in1 = [10,5,2,7,8,7]
#in2 = 3

in1 = range(0, 100000 + 1)
in2 = 100

findSubMax(in1,in2)
