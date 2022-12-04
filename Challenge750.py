"""
Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""
import random

class IfiniTree:
    l = None
    r = None
    val = None

    def __init__(self, Bounds = 10, left = None, right = None):
        self.val = random.randint(1, 1000)
        if Bounds > 0:
            Bounds -= 1
            self.l = IfiniTree(Bounds)
        if Bounds > 0:
            Bounds -= 1
            self.r = IfiniTree(Bounds)
        

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

# Return a random large binary tree.
in1 = IfiniTree(15)
printBinaryTree(in1)