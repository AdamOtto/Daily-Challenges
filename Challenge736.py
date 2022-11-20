"""
Given a complete binary tree, count the number of nodes in faster than O(n) time.
Recall that a complete binary tree has every level filled except the last,
and the nodes in the last level are filled starting from the left.
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

def Solution(tr):
    bot = getBottom(tr)
    nulls = FindNulls(tr, 1, bot)
    return pow(2, bot) - nulls - 1
    
def getBottom(ar):
    if ar is None:
        return 1
    return 1 + getBottom(ar.r)

def FindNulls(ar, level, bottom):
    if ar is None or level > bottom:
        if level == bottom:
            return 1
        return 0
    return FindNulls(ar.l, level + 1, bottom) + FindNulls(ar.r, level + 1, bottom)
    
    

# Return 6
in1 = Tree(1, Tree(2,Tree(4), Tree(5)), Tree(3, Tree(6)))
printBinaryTree(in1)
print(Solution(in1))

print()

# Return 5
in1 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3))
printBinaryTree(in1)
print(Solution(in1))

print()

# Return 8
in1 = Tree(1, Tree(2, Tree(4, Tree(8)), Tree(5)), Tree(3, Tree(6), Tree(7)))
printBinaryTree(in1)
print(Solution(in1))