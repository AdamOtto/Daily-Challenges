"""
Given a binary tree, determine whether or not it is height-balanced.
A height-balanced binary tree can be defined as one in which the heights
of the two subtrees of any node never differ by more than one.
"""

class BTree:
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


def Solution(tr):
    l = dig(tr.l)
    r = dig(tr.r)
    if l == r:
        return True
    elif l == r + 1 or l == r - 1:
        return True
    return False

def dig(tr):
    if tr is None:
        return 0
    return max(dig(tr.l), dig(tr.r)) + 1

in1 = BTree(1, BTree(2, BTree(4),BTree(5)), BTree(3,None, BTree(6)))
printBinaryTree(in1)
print("height-balanced: " + str(Solution(in1)))
print()

in1 = BTree(1, BTree(2, BTree(4),BTree(5)), BTree(3,None, BTree(6,BTree(7), BTree(8))))
printBinaryTree(in1)
print("height-balanced: " + str(Solution(in1)))
print()

in1 = BTree(1, BTree(2, BTree(4),BTree(5)), BTree(3,None, BTree(6,BTree(7, BTree(9), BTree(10)), BTree(8))))
printBinaryTree(in1)
print("height-balanced: " + str(Solution(in1)))
print()