"""
Given a set of points (x, y) on a 2D cartesian plane, find the two closest points.
For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)],
return [(-1, -1), (1, 1)].
"""
import sys
import math

def Solution(ar):
    l = len(ar)
    shortest = sys.maxsize
    retVal = None
    for i in range(l):
        for j in range(i + 1, l):
            dx = ar[i][0] - ar[j][0]
            dy = ar[i][1] - ar[j][1]
            if math.sqrt(dx ** 2 + dy ** 2) < shortest:
                shortest = math.sqrt(dx ** 2 + dy ** 2)
                retVal = (ar[i], ar[j])
    return retVal

in1 = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]
print(Solution(in1))