"""
Given a binary tree of integers, find the maximum path sum between two nodes.
The path must go through at least one node, and does not need to go through the root.
"""
class Tree:
    l = None
    r = None
    val = None

    def __init__(self, value, left = None, right = None):
        self.l = left
        self.r = right
        self.val = value

def Solution(ar):
    if ar is None:
        return 0
    l = Solution(ar.l)
    r = Solution(ar.r)
    max1 = max((max(l, r) + ar.val, ar.val))
    return max(max1, l + r + ar.val)

# Return 6
in1 = Tree(2, Tree(1), Tree(3))
print(Solution(in1))

# Return 43
in1 = Tree(10, Tree(2, Tree(20), Tree(1)), Tree(10, None, Tree(-25, Tree(3), Tree(4))))
print(Solution(in1))