"""
Suppose you are given two lists of n points, one list p1, p2, ...,
pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1.
Imagine a set of n line segments connecting each point pi to qi.

Write an algorithm to determine how many pairs of the line segments intersect.
"""

# Determine slope of each line pair.  If two lines have the same slope, they will not intersect.
# O(n)
def Solution(q1, q2):
    n = len(q1)
    if n != len(q2):
        return False
    intersect = 0
    slopes = {}
    for i in range(0, n):
        slope = q2[i] - q1[2]
        if slope not in slopes:
            intersect += len(slopes)
            slopes[slope] = slope
        else:
            intersect += len(slopes) - 1
    return intersect


in1 = [1, 3, 5, 4, 6, 2]
in2 = [2, 1, 5, 4, 3, 6]
print(Solution(in1, in2))
