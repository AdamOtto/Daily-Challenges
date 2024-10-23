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

def Solution(ar, rng):
    if ar is None:
        return 0
    t = 0
    if ar.val >= rng[0] and ar.val <= rng[1]:
        t += ar.val
    t += Solution(ar.l, rng)
    t += Solution(ar.r, rng)
    return t

# Return 23
in1 = Tree(5, Tree(3, Tree(2), Tree(4)), Tree(8, Tree(6), Tree(10)))
print(Solution(in1, [4, 9]))

# Return 18
in1 = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
print(Solution(in1, [3, 6]))