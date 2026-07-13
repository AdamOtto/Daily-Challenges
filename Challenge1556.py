"""
Write a program to merge two binary trees.
Each node in the new tree should hold a value equal to the sum of the
values of the corresponding nodes of the input trees.

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

def Solution(in1, in2):
    t = Tree(0)
    if in1 is None and in2 is None:
        return None
    if in1 is None:
        t.val = in2.val
        t.l = Solution(None, in2.l)
        t.r = Solution(None, in2.r)
    elif in2 is None:
        t.val = in1.val
        t.l = Solution(in1.l, None)
        t.r = Solution(in1.r, None)
    else:
        t.val = in1.val + in2.val
        t.l = Solution(in1.l, in2.l)
        t.r = Solution(in1.r, in2.r)
    return t


in1 = Tree(1, Tree(2), Tree(3))
in2 = Tree(4, Tree(3, Tree(1), Tree(3)), Tree(2, Tree(1), Tree(1)))
printBinaryTree(Solution(in1, in2))