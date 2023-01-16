"""
Recall that a full binary tree is one in which each node is
either a leaf node, or has two children. Given a binary tree,
convert it to a full one by removing nodes with only one child.
For example, given the following tree:
         0
      /     \
    1         2
  /            \
3                 4
  \             /   \
    5          6     7
You should convert it to:
     0
  /     \
5         4
        /   \
       6     7
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
    ar.l = Helper(ar.l)
    ar.r = Helper(ar.r)
    return ar

def Helper(curNode):
    if curNode is None:
        return None

    if curNode.l is not None and curNode.r is not None:
        return curNode
    elif curNode.l is None and curNode.r is None:
        return curNode

    if curNode.l is not None:
        curNode = Helper(curNode.l)
    elif curNode.r is not None:
        curNode = Helper(curNode.r)
    return curNode

# Return the tree given in the example.
in1 = Tree(0, Tree(1,Tree(3,None, Tree(5))), Tree(2, None, Tree(4, Tree(6), Tree(7))))
Solution(in1)
printBinaryTree(in1)