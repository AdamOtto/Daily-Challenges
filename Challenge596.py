"""
Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
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

def Solution(ar):
    if ar is None:
        return
    temp = ar.l
    ar.l = ar.r
    ar.r = temp
    
    Solution(ar.l)
    Solution(ar.r)
    return

# Return inverted tree
in1 = Tree("a", Tree('b', Tree('d'), Tree('e')), Tree('c', Tree('f'), None))
printBinaryTree(in1)
Solution(in1)
printBinaryTree(in1)

print('\n')

# Return inverted tree
in1 = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
printBinaryTree(in1)
Solution(in1)
printBinaryTree(in1)
