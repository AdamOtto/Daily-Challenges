"""
Two nodes in a binary tree can be called cousins if they are on
the same level of the tree but have different parents.
For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \   \
4   5   6

Given a binary tree and a particular node, find all cousins of that node.
"""

class Tree:
    l = None
    r = None
    val = None

    def __init__(self, value, left = None, right = None):
        self.l = left
        self.r = right
        self.val = value


def Solution(tree, nodeInt):
    retVal = []
    if tree.val == nodeInt:
        return retVal
    
    curLevel = []
    curLevel.append( (tree, tree.val) )
    nextLevel = []
    
    nodeIntFound = False
    nodeIntParent = None
    
    while nodeIntFound is False:
        while len(curLevel) > 0:
            temp = curLevel.pop()
            if temp[0].l is not None and temp[0].l.val == nodeInt:
                nodeIntFound = True
                nodeIntParent = temp[0].val
            elif temp[0].r is not None and temp[0].r.val == nodeInt:
                nodeIntFound = True
                nodeIntParent = temp[0].val
            nextLevel.append( (temp[0].l, temp[0].val) )
            nextLevel.append( (temp[0].r, temp[0].val) )
        curLevel = nextLevel
        nextLevel = []
    
    for c in curLevel:
        if c[0] is not None and c[1] != nodeIntParent:
            retVal.append(c[0].val)
    return retVal
    
    

in1 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, None, Tree(6)))
print(Solution(in1, 4))
print(Solution(in1, 6))