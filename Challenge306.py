"""
You are given a list of N numbers,
in which each number is located at most k places away from its sorted position.
For example, if k = 1, a given element at index 4 might end up at indices 3, 4, or 5.

Come up with an algorithm that sorts this list in O(N log k) time.
"""
from heapq import heappop, heappush, heapify

def Solution(N, k):
    l = len(N)
    h = N[:k + 1]
    heapify(h)

    ind = 0
    for i in range(k + 1, l):
        N[ind] = heappop(h)
        heappush(h, N[i])
        ind += 1
    while h:
        N[ind] = heappop(h)
        ind += 1
    return N

print(Solution([6, 5, 3, 2, 8, 10, 9], 3))

print(Solution([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10))