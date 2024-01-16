"""
Given a binary tree, return the level of the tree with minimum sum

Assume top of tree is level 1, each node below it is level 1+n
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
    return Helper(ar)[1]

def Helper(ar, level = 1):
    if ar is None:
        return (0, level - 1)
    l = Helper(ar.l, level + 1)
    r = Helper(ar.r, level + 1)
    if l[0] < r[0]:
        return (ar.val + l[0], l[1])
    else:
        return (ar.val + r[0], r[1])

# Return 3
in1 = Tree(1, Tree(1, Tree(1), Tree(1)), Tree(5))
print(Solution(in1))

# Return 3
in1 = Tree(1, Tree(10), Tree(2, Tree(3), Tree(5)))
print(Solution(in1))

# Return 2
in1 = Tree(1, Tree(1), Tree(2, Tree(3), Tree(5)))
print(Solution(in1))