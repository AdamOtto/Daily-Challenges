"""
Given a binary tree, find the lowest common
ancestor (LCA) of two given nodes in the tree.
Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as
the lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself).”

Assumumptions:
All values in the tree are unique.
Tree is not necessarily balanced.
"""

class Tree:
    p = None
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

def setTreeParents(ar):
    if ar is None:
        return
    if ar.l is not None:
        ar.l.p = ar
        setTreeParents(ar.l)
    if ar.r is not None:
        ar.r.p = ar
        setTreeParents(ar.r)
    return
    
def Solution(ar, n1, n2):
    node1 = findNode(ar, n1)
    node2 = findNode(ar, n2)
    
    n1Ancestors = []
    n2Ancestors = []
    
    getAncestors(node1.p, n1Ancestors)
    getAncestors(node2.p, n2Ancestors)
    
    intersect = list(set(n1Ancestors) & set(n2Ancestors))
    if len(intersect) == 0:
        return None
    
    retVal = None
    level = -1
    for i in intersect:
        nodeLevel = getLevel(ar, i)
        if nodeLevel > level:
            retVal = i
            level = nodeLevel
    return retVal
    
def findNode(cur, n):
    if cur is None:
        return None
    if cur.val == n:
        return cur
    
    t = findNode(cur.l, n)
    if t is not None:
        return t
    t = findNode(cur.r, n)
    if t is not None:
        return t
    return None

def getAncestors(cur, ancestors):
    if cur is None:
        return
    ancestors.append(cur.val)
    getAncestors(cur.p, ancestors)

def getLevel(cur, node, l = 0):
    if cur == None:
        return None
    if cur.val == node:
        return l
    
    t = getLevel(cur.l, node, l+1)
    if t is not None:
        return t
    t = getLevel(cur.r, node, l+1)
    if t is not None:
        return t

# Return 6
in1 = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
printBinaryTree(in1)
setTreeParents(in1)
print("LCA of 5 and 7:", Solution(in1, 5, 7), "\n")


# Return 9
in1 = Tree(8, Tree(7, Tree(3, Tree(1), Tree(2)), Tree(6, Tree(4), Tree(5))), Tree(9, Tree(10, Tree(11), Tree(12)), Tree(13, Tree(14), Tree(15))))
printBinaryTree(in1)
setTreeParents(in1)
print("LCA of 11 and 13:", Solution(in1, 11, 13))

# Return 8
print("LCA of 1 and 15:", Solution(in1, 1, 15))

# Return None
print("LCA of 8 and 4:", Solution(in1, 8, 4))