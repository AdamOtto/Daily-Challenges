"""
Given a set of points (x, y) on a 2D cartesian plane,
find the two closest points.
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

# Return ((1, 1), (-1, -1))
print(Solution([(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]))

# Return ((100, 40), (89, 33))
print(Solution([(100,40),(49,14),(53,98),(25,13),(70,48),(144,47),(90,90),(89,33),(24,54)]))