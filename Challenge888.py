"""
Given a list of points, a central point, and an integer k,
find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)],
the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
"""
import math

def Solution(ar, center, k):
    l = len(ar)
    if k > l:
        return None
    lengths = []
    for i in range(l):
        lengths.append( ( math.sqrt(abs( (center[0] ** 2) - (ar[i][0] ** 2) ) + abs( (center[1] ** 2) - (ar[i][1] ** 2) )), i))
    
    lengths.sort(key=lambda tup: tup[0])
    retVal = []
    for i in range(k):
        retVal.append(ar[lengths[i][1]])
    return retVal


# Return [(0, 0), (3, 1)]
print(Solution([(0, 0), (5, 4), (3, 1)], (1, 2), 2))

# Return [(24, 36), (10, 14), (6, -10), (40, 45)]
print(Solution([(10, 14), (6, -10), (50, 1), (40, 45), (24, 36)], (23, 30), 4))