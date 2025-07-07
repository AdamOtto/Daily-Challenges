"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a set of points (x, y) on a 2D cartesian plane,
find the two closest points.
For example, given the points
[(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)],
return [(-1, -1), (1, 1)]
"""
import math
def Solution(ar):
    l = len(ar)
    dist = None
    retVal = None
    for a in range(l - 1):
        for r in range(a + 1, l):
            temp = math.sqrt( pow(ar[a][0] - ar[r][0],2) + pow(ar[a][1] - ar[r][1],2) )
            if dist is None:
                dist = temp
                retVal = ( ar[a], ar[r] )
            elif temp < dist:
                dist = temp
                retVal = ( ar[a], ar[r] )
            
    return retVal

# Return ((1, 1), (-1, -1))
print(Solution( [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)] ))

# Return ((0, 0), (0, 5))
print(Solution( [(0,0), (0,5), (5,5), (5,0)] ))