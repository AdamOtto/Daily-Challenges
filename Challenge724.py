"""
Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
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
        return 0
    
    if isinstance(ar.val, int):
        return ar.val
    if ar.val == "*":
        return Solution(ar.l) * Solution(ar.r)
    if ar.val == "/":
        return Solution(ar.l) / Solution(ar.r)
    if ar.val == "+":
        return Solution(ar.l) + Solution(ar.r)
    if ar.val == "-":
        return Solution(ar.l) - Solution(ar.r)
    return None

# Return 45
in1 = Tree("*", Tree("+", Tree(3), Tree(2)), Tree("+", Tree(4), Tree(5)))
print(Solution(in1))

# Return 18
in1 = Tree("*", Tree("+", Tree("/",Tree(6), Tree(2)), Tree(3)), Tree("-", Tree("*", Tree(2), Tree(4)), Tree(5)))
print(Solution(in1))