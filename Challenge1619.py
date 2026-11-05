"""
Given two non-empty binary trees s and t,
check whether tree t has exactly the same
structure and node values with a subtree of s.

A subtree of s is a tree consists of a node in s
and all of this node's descendants.
The tree s could also be considered as a subtree of itself.
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

def Solution(s, t):
    treeS = Helper(s)
    treeT = Helper(t)
    return subfinder(treeS, treeT)

def Helper(ar):
    if ar is None:
        return []
    retVal = []
    retVal.append(ar.val)
    retVal = Helper(ar.l) + retVal
    retVal = retVal + Helper(ar.r)
    return retVal

def subfinder(mylist, pattern):
    matches = []
    for i in range(len(mylist)):
        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
            matches.append(pattern)
    if len(matches) >= 1:
        return True
    return False

# Return True
s = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
t = Tree(2, Tree(1), Tree(3))
print(Solution(s, t))

# Return True
s = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
t = Tree(7)
print(Solution(s, t))

# Return True
s = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
t = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
print(Solution(s, t))

# Return False
s = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
t = Tree(5, Tree(4, Tree(6), Tree(8)), Tree(3, Tree(2), Tree(1)))
print(Solution(s, t))

# Return False
s = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6))
t = Tree(4, Tree(2), Tree(6))
print(Solution(s, t))