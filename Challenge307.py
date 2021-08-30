"""
Given a binary search tree, find the floor and ceiling of a given integer.
The floor is the highest element in the tree less than or equal to an integer,
while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.
"""
import sys

class Tree:
    l = None
    r = None
    val = None

    def __init__(self, value, left = None, right = None):
        self.l = left
        self.r = right
        self.val = value

def Solution(ar, k):
    floor = -sys.maxsize
    ceiling = sys.maxsize
    floor, ceiling = Helper(ar, k, floor, ceiling)
    return (floor, ceiling)
    
def Helper(ar, k, floor, ceiling):
    if ar is None:
        return (-sys.maxsize, sys.maxsize)
    
    if ar.val >= k:
        ceiling = min(ar.val, ceiling)
    if ar.val <= k:
        floor = max(ar.val, floor)
    t = Helper(ar.l, k, floor, ceiling)
    floor = max(t[0], floor)
    ceiling = min(t[1], ceiling)
    t = Helper(ar.r, k, floor, ceiling)
    floor = max(t[0], floor)
    ceiling = min(t[1], ceiling)
    return (floor, ceiling)

# Returns 5, 5
in1 = Tree(4,Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
print("(floor, ceiling) = ", Solution(in1, 5))

# Returns (600, 943)
in1 = Tree(500, Tree(400, Tree(100), Tree(450)), Tree(943, Tree(600), Tree(1000)))
print("(floor, ceiling) = ", Solution(in1, 650))