"""
You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN) representing a polygon.
You can assume these points are given in order; that is, you can construct the
polygon by connecting point 1 to point 2, point 2 to point 3, and so on,
finally looping around to connect point N to point 1.

Determine if a new point p lies inside this polygon.
(If p is on the boundary of the polygon, you should return False).
"""
from sympy.geometry import *
import sys

def Solution(polyPoints, point):
    l = len(polyPoints)
    poly = []
    for i in range(1, l):
        poly.append( Segment(polyPoints[i - 1], polyPoints[i]) )
    poly.append( Segment(polyPoints[l - 1], polyPoints[0]) )

    pointLine = Segment( point, (sys.maxsize, point[1]) )

    l2 = len(poly)
    count = 0
    for i in range(0, l2):
        if len(intersection(poly[i], pointLine)) >= 1:
            count += 1

    if count % 2 == 0 or count == 0:
        return False
    else:
        return True



in1 = [ (0,0), (0, 5), (5,5), (5,0) ]
in2 = (2,2)
print(Solution(in1, in2))
in3 = (6,0)
print(Solution(in1, in3))