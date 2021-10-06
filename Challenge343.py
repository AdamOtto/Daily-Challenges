"""
Given a binary search tree and a range [a, b] (inclusive),
return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).
"""

class Tree:
    l = None
    r = None
    val = None

    def __init__(self, value, left = None, right = None):
        self.l = left
        self.r = right
        self.val = value

def Solution(tree, sumRange):
    if tree is None:
        return 0
    if tree.val >= sumRange[0] and tree.val <= sumRange[1]:
        return tree.val + Solution(tree.l, sumRange) + Solution(tree.r, sumRange)
    return Solution(tree.l, sumRange) + Solution(tree.r, sumRange)

tree = Tree(5, Tree(3, Tree(2), Tree(4)), Tree(8, Tree(6), Tree(10)))
print(Solution(tree, [4,9]))