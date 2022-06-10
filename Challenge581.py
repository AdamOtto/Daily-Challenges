"""
Given two rectangles on a 2D graph, return the area of their intersection.
If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
"""
class rect:
    left = None
    right = None
    top = None
    bottom = None
    def __init__(self, ar):
        self.left = ar["top_left"][0]
        self.right = ar["top_left"][0] + ar["dimensions"][0]
        self.top = ar["top_left"][1]
        self.bottom = ar["top_left"][1] - ar["dimensions"][1]

def Solution(ar1, ar2):
    r1 = rect(ar1)
    r2 = rect(ar2)
    xOverlap = max(0, min(r1.right, r2.right) - max(r1.left, r2.left))
    yOverlap = max(0, min(r1.top, r2.top) - max(r1.bottom, r2.bottom))
    return xOverlap * yOverlap

# Return 6
rec1 = {"top_left": (1, 4),
        "dimensions": (3, 3)}
rec2 = {"top_left": (0, 5),
        "dimensions": (4, 3)}
print(Solution(rec1, rec2))

# Return 1
rec1 = {"top_left": (0, 100),
        "dimensions": (100, 100)}
rec2 = {"top_left": (0, 50),
        "dimensions": (1, 1)}
print(Solution(rec1, rec2))

# Return 0
rec1 = {"top_left": (0, 100),
        "dimensions": (100, 100)}
rec2 = {"top_left": (101, 50),
        "dimensions": (1, 1)}
print(Solution(rec1, rec2))