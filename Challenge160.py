"""
Given a tree where each edge has a weight,
compute the length of the longest path in the tree from the root.
"""

class treeNode:

    val = None
    d = None

    def __init__(self, Value, Edges = None):
        if Edges is not None:
            self.d = Edges
        else:
            self.d = {}
        self.val = Value


def Solution(tree):
    retVal = 0
    for key, val in tree.d.items():
        t = Solution(key) + val
        if t > retVal:
            retVal = t
    return retVal

t1 = treeNode("g")
t2 = treeNode("h")
t3 = treeNode("e", {t1:1, t2:1})
t4 = treeNode("f")
t5 = treeNode("d", {t3:2, t4:4})
t6 = treeNode("c")
t7 = treeNode("b")
in1 = treeNode("a", {t5:8, t6:5, t7:3})
print(Solution(in1))