"""
Write a program to merge two binary trees.
Each node in the new tree should hold a value equal to the sum of the values
of the corresponding nodes of the input trees.

If only one input tree has a node in a given position,
the corresponding node in the new tree should match that input node.
"""

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

def Solution(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    retVal = Tree(t1.val + t2.val)
    retVal.l = Helper(t1.l, t2.l)
    retVal.r = Helper(t1.r, t2.r)
    
    return retVal

def Helper(t1, t2):
    if t1 is None and t2 is None:
        return None
    ret = Tree(0)
    if t1 is None:
        ret.val = t2.val
        ret.l = Helper(None, t2.l)
        ret.r = Helper(None, t2.l)
    elif t2 is None:
        ret.val = t1.val
        ret.l = Helper(t1.l, None)
        ret.r = Helper(t1.r, None)
    else:
        ret.val = t1.val + t2.val
        ret.l = Helper(t1.l, t2.l)
        ret.r = Helper(t1.r, t2.r)
    return ret

"""
Return
'6' 
'3' '9' 
'1' '2' '5' '7' 
_ _ _ _ _ _ _ _
"""
t1 = Tree(2, Tree(1, None, Tree(-1)), Tree(3))
printBinaryTree(t1)
print()
t2 = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
printBinaryTree(t2)
print()
printBinaryTree(Solution(t1, t2))