"""
The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

    The horizontal distance of the root is 0.
    The horizontal distance of a left child is hd(parent) - 1.
    The horizontal distance of a right child is hd(parent) + 1.

    For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8

The bottom view of a tree, then, consists of the lowest node at each horizontal distance.
If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9] or [0, 1, 3, 4, 8, 9].

Given the root to a binary tree, return its bottom view.
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
            printStr += str(queue[0].val) + " "
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
    retVal = []
    d = {}
    Helper(ar, d, 0, 0)
    #print(d)
    for key, val in d.items():
        retVal.append(val[0])
    return sorted(retVal)

def Helper(ar, d, level, HorDist):
    if ar is None:
        return
    if HorDist in d:
        if d[HorDist][1] < level:
            d[HorDist] = (ar.val, level)
    else:
        d[HorDist] = (ar.val, level)

    Helper(ar.l, d, level + 1, HorDist - 1)
    Helper(ar.r, d, level + 1, HorDist + 1)

in1 = Tree(5, Tree(3, Tree(1, Tree(0)), Tree(4)), Tree(7, Tree(6), Tree(9, Tree(8))))
printBinaryTree(in1)
print(Solution(in1))
print()
print()

in1 = Tree(10, Tree(5, Tree(3, Tree(1), Tree(4)), Tree(8, Tree(7), Tree(9))), Tree(15, Tree(13, Tree(11), Tree(18, Tree(16), Tree(19))), Tree(25, Tree(20), Tree(30))))
printBinaryTree(in1)
print(Solution(in1))
