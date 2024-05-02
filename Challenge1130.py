"""
Given a tree, return the size of the largest tree/subtree that is a BST.

Notes:
Help from
https://www.geeksforgeeks.org/largest-bst-binary-tree-set-2/
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


def Solution(root):
    if root is None:
        return 0, -sys.maxsize, sys.maxsize, 0, True
    if root.l is None and root.r is None:
        return 1, root.val, root.val, 1, True
    
    
    l = Solution(root.l)
    r = Solution(root.r)
    
    retVal = [0,0,0,0,0]
    retVal[0] = 1 + l[0] + r[0]
    
    if l[4] and r[4] and l[1] < root.val and r[2] > root.val:
        retVal[1] = max(r[1], max(l[1], root.val))
        retVal[2] = min(l[2], min(r[2], root.val))
        retVal[3] = retVal[0]
        retVal[4] = True
        return retVal
    
    retVal[3] = max(l[3], r[3])
    retVal[4] = False
    return retVal


# Return 2
in1 = Tree(60, Tree(65, Tree(50)), Tree(70))
print(Solution(in1)[3])


# Return 3
in1 = Tree(10, Tree(5, Tree(3), Tree(7)), Tree(15, Tree(16), Tree(13)))
print(Solution(in1)[3])