"""
Given a set of points (x, y) on a 2D cartesian plane, find the two closest points.
For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)],
return [(-1, -1), (1, 1)].
"""
import sys
import math
def Solution(ar):
    l = len(ar)
    dist = sys.maxsize
    retVal = ()
    for i in range(0, l):
        for j in range(i + 1, l):
            if getDistance(ar[i], ar[j]) < dist:
                dist = getDistance(ar[i], ar[j])
                retVal = (ar[i], ar[j])
    return retVal

def getDistance(ar1, ar2):
    return math.sqrt( math.pow(ar1[0] - ar2[0], 2) + math.pow(ar1[1] - ar2[1], 2))


# Return ((1, 1), (-1, -1))
print(Solution([(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]))
# Return ((2, 0), (8, 0))
print(Solution([(2,0), (-4,4), (-1,-6), (8,0)]))