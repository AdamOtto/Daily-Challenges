"""
Two nodes in a binary tree can be called cousins if they are
on the same level of the tree but have different parents.
For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \   \
4   5   6

Given a binary tree and a particular node,
find all cousins of that node.
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

# O(n)
def Solution(ar, k):
    if ar.val == k:
        return None
    parent, level = findNode(None, ar, k, 0)
    retVal = []
    findCousins(parent, ar, 0, level, retVal)
    return retVal

def findNode(parent, cur, k, level):
    if cur is None:
        return None
    if cur.val == k:
        return (parent, level)
    
    temp = findNode(cur.val, cur.l, k, level + 1)
    if temp is not None:
        return temp
    temp = findNode(cur.val, cur.r, k, level + 1)
    if temp is not None:
        return temp
    return None

def findCousins(parent, cur, curlevel, level, retVal):
    if cur is None:
        return
    if cur.val == parent:
        return
    if curlevel > level:
        return
    if curlevel == level:
        retVal.append(cur.val)
        return
    findCousins(parent, cur.l, curlevel + 1, level, retVal)
    findCousins(parent, cur.r, curlevel + 1, level, retVal)
    return

# Return [6]
in1 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, None, Tree(6)))
#printBinaryTree(in1)
print(Solution(in1, 4))



# Return [8, 9, 11, 12, 14, 15]
in1 = Tree(1, Tree(2, Tree(4, Tree(6), Tree(7)), Tree(5, Tree(8), Tree(9))), Tree(3, Tree(10, Tree(11), Tree(12)), Tree(13, Tree(14), Tree(15))))
#printBinaryTree(in1)
print(Solution(in1, 6))