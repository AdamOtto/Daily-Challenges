"""
Write a program to merge two binary trees. Each node in the new tree should hold
a value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node
in the new tree should match that input node.
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


def Solution(t1, t2):
    if t1 is None and t2 is None:
        return None
    if t1 is not None and t2 is None:
        return t1
    if t1 is None and t2 is not None:
        return t2
    
    retVal = Tree( t1.val + t2.val )
    retVal.l = Solution(t1.l, t2.l)
    retVal.r = Solution(t1.r, t2.r)
    return retVal

print("Tree 1")
t1 = Tree(7, Tree(5, Tree(1), Tree(2)), Tree(6, Tree(3), Tree(4)))
printBinaryTree(t1)
print("\nTree 2")
t2 = Tree(1, Tree(2), Tree(3, None, Tree(2, Tree(4), Tree(5))))
printBinaryTree(t2)
print("\nMerged tree")
t3 = Solution(t1, t2)
printBinaryTree(t3)