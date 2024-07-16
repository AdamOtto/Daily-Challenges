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
        lengths.append( (getDistance(ar[i], center), ar[i]) )
    
    lengths.sort(key=lambda tup: tup[0])
    
    retVal = []
    for i in range(k):
        retVal.append(lengths[i][1])
    return retVal

def getDistance(p1, p2):
    return math.sqrt( math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2) )

# Return [(0, 0), (3, 1)]
print(Solution([(0, 0), (5, 4), (3, 1)], (1, 2), 2))

# Return [(24, 36), (10, 14), (40, 45), (50, 1)]
print(Solution([(10, 14), (6, -10), (50, 1), (40, 45), (24, 36)], (23, 30), 4))