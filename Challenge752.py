"""
Print the nodes in a binary tree level-wise.
For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
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
    if not isinstance(ar, Tree):
        return None
    retVal = ""
    retVal += str(ar.val) + ", "
    q = []
    q.append(ar.l)
    q.append(ar.r)
    
    while len(q) > 0:
        temp = q.pop(0)
        if temp is not None:
            retVal += str(temp.val) + ", "
            q.append(temp.l)
            q.append(temp.r)
    return retVal[0:-2]

# Return 1, 2, 3, 4, 5
in1 = Tree(1, Tree(2), Tree(3, Tree(4), Tree(5)))
print(Solution(in1))


# Return 1, 2, 3, 4, 5, 6, 7
in1 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
print(Solution(in1))

# Return 10, 15, 40, 1, 45, 50, 60
in1 = Tree(10, Tree(15, None, Tree(1)), Tree(40, Tree(45, None, Tree(60)), Tree(50)))
print(Solution(in1))