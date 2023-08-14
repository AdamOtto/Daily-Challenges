"""
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
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
    retVal = []
    Helper(ar, retVal, 0)

def Helper(cur, retVal, pathLen):
    if cur is None:
        return
    if len(retVal) > pathLen:
        retVal[pathLen] = cur.val
    else:
        retVal.append(cur.val)
    
    pathLen += 1
    
    if cur.l is None and cur.r is None:
        printArray(retVal, pathLen)
    else:
        Helper(cur.l, retVal, pathLen)
        Helper(cur.r, retVal, pathLen)

def printArray(ints, pathLen):
    for i in ints[0 : pathLen]:
        print(i," ",end="")
    print()

# return 1  2, 1  3  4, 1  3  5
in1 = Tree(1, Tree(2), Tree(3, Tree(4), Tree(5)))
Solution(in1)

print()

# Return 4  2  1, 4  2  3, 4  6  5, 4  6  7 
in1 = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
Solution(in1)