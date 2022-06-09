"""
Given a binary tree, find a
minimum path sum from root to a leaf.

For example, the minimum path in this
tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \    \
  2    1
      /
    -1
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

def Solution(ar):
    if ar is None:
        return sys.maxsize
    if ar.l is None and ar.r is None:
        return ar.val
    
    return min(ar.val + Solution(ar.l), ar.val + Solution(ar.r))

# Return 15
in1 = Tree(10, Tree(5, None, Tree(2)), Tree(5, None, Tree(-1, Tree(1))))
print(Solution(in1))

# Return 7
in1 = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
print(Solution(in1))