"""
Given a binary search tree and a range [a, b] (inclusive),
return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).
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

def Solution(tree, ran):
    if tree is None:
        return 0
    if tree.val in range(ran[0], ran[1] + 1):
        return tree.val + Solution(tree.l, ran) + Solution(tree.r, ran)
    return Solution(tree.l, ran) + Solution(tree.r, ran)

# Return 23
in1 = Tree(5, Tree(3, Tree(2), Tree(4)), Tree(8, Tree(6), Tree(10)))
printBinaryTree(in1)
print("Sum in range [4,9]:", Solution(in1, [4,9]))

# Return 0
in1 = Tree(2, Tree(1), Tree(3))
printBinaryTree(in1)
print("Sum in range [4,9]:", Solution(in1, [4,9]))