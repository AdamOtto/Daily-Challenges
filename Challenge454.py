"""
Given the root of a binary search tree, and a target K,
return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
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

def Solution(ar, k):
    s = set()
    FillSet(s, ar)
    s = list(s)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] + s[j] == k:
                return s[i], s[j]
    return None
    

def FillSet(s, ar):
    if ar is None:
        return
    s.add(ar.val)
    FillSet(s, ar.l)
    FillSet(s, ar.r)
    return

# Return (5, 15)
in1 = Tree(10, Tree(5), Tree(15, Tree(11), Tree(15)))
#printBinaryTree(in1)
print(Solution(in1, 20))