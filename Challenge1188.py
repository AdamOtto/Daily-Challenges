"""
We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions.
The array [2, 4, 1, 3, 5] has three inversions:
(2, 1), (4, 1), and (4, 3).
The array [5, 4, 3, 2, 1] has ten inversions:
every distinct pair forms an inversion.
"""
from heapq import heappush, heappop
from bisect import bisect, insort
  
# O(nlog(n))
def Solution(A):
    N = len(A)
    if N <= 1:
        return 0
  
    sortList = []
    result = 0
  
    for i, v in enumerate(A):
        heappush(sortList, (v, i))
  
    x = []
    while sortList:
        v, i = heappop(sortList)
        y = bisect(x, i)
        result += i - y
        insort(x, i)
  
    return result

# Return 3
print(Solution([2, 4, 1, 3, 5]))
# Return 10
print(Solution([5, 4, 3, 2, 1]))
# Return 0
print(Solution([1, 2, 3, 4, 5]))
# Return 14
print(Solution([1,10,3,4,2,7,5,8,9,6]))