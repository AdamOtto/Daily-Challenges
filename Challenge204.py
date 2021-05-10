"""
Given a complete binary tree, count the number of nodes in faster than O(n) time.
Recall that a complete binary tree has every level filled except the last,
and the nodes in the last level are filled starting from the left.
"""

class tree:
    l = None
    r = None
    val = None

    def __init__(self, value, left = None, right = None):
        self.val = value
        self.l = left
        self.r = right

def Solution(tr):
    bottomNodes = []
    GetBottomNodes(tr, bottomNodes)
    level = getLevel(tr)
    if len(bottomNodes) == pow(2, level - 1):
        return pow(2, level) - 1
    else:
        return pow(2, level) + len(bottomNodes) - 1

def GetBottomNodes(ar, bottomNodes):
    if ar is None:
        return
    if ar.l == None or ar.r == None:
        bottomNodes.append(ar)
        return
    if not ar.l == None:
        GetBottomNodes(ar.l, bottomNodes)
    if not ar.r == None:
        GetBottomNodes(ar.r, bottomNodes)
    return

def getLevel(ar):
    if ar == None:
        return 0
    return getLevel(ar.r) + 1


in1 = tree(1, tree(2,tree(4), tree(5)), tree(3, tree(6)))
print(Solution(in1))