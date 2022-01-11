"""
Given a binary tree, return the level of the tree with minimum sum.
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

def printBinaryTree(bt):
    layer = 1
    count = 0
    printStr = ""
    queue = []
    queue.append(bt)

    while len(queue) != 0:

        if queue[0] is not None:
            if queue[0].val is not None:
                printStr += "\'" + str(queue[0].val) + "\' "
            else:
                printStr += "_ "
            queue.append(queue[0].l)
            queue.append(queue[0].r)
        else:
            printStr += "_ "

        queue.pop(0)
        count += 1
        if count == layer:
            layer = len(queue)
            count = 0
            print(printStr)
            printStr = ""


def Solution(ar, minVal = sys.maxsize):
    if ar is None:
        return 0
    if ar.l is None and ar.r is None:
        return ar.val
    left = Helper(ar.l, 2)
    right = Helper(ar.r, 2)
    
    if left[0] + ar.val < right[0] + ar.val:
        return left[1]
    else:
        return right[1]

def Helper(ar, level):
    if ar is None:
        return 0, level
    if ar.l is None and ar.r is None:
        return ar.val, level
    left = right = (sys.maxsize, sys.maxsize)
    if ar.l is not None:
        left = Helper(ar.l, level + 1)
    if ar.r is not None:
        right = Helper(ar.r, level + 1)
    if left[0] + ar.val < right[0] + ar.val:
        return (left[0] + ar.val, left[1])
    else:
        return (right[0] + ar.val, right[1])

# Should return 3.  Lowest sum is 4 + 2 + 1, 1 is on level 3 if we consider 4 is on level 1.
in1 = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
print(Solution(in1))