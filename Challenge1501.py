"""
For example, given the following tree:

  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
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
    d = {}
    Helper(ar, d)
    return max(d, key=d.get)

def Helper(tree, d):
    if tree is None:
        return 0
    temp = tree.val + Helper(tree.l, d) + Helper(tree.r, d)
    if temp not in d:
        d[temp] = 0
    d[temp] += 1
    return temp

# Return 2
in1 = Tree(5, Tree(2), Tree(5))
print(Solution(in1))

# Return 4
in1 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
print(Solution(in1))