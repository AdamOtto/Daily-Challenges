"""
Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:

   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
"""



class BinaryTree:
    left = None
    right = None
    val = None

    def __init__(self, value, leftNode, rightNode):
        self.val = value
        self.left = leftNode
        self.right = rightNode


def printBinaryTree(bt):
    layer = 1
    count = 0
    printStr = ""
    queue = []
    queue.append(bt)

    while len(queue) != 0:

        if queue[0] is not None:
            printStr += str(queue[0].val) + " "
            queue.append(queue[0].left)
            queue.append(queue[0].right)
        else:
            printStr += "_ "

        queue.pop(0)
        count += 1
        if count == layer:
            layer = len(queue)
            count = 0
            print(printStr)
            printStr = ""


def Solution(bt):
    queue = []
    queue.append(bt)

    while len(queue) != 0:
        if CheckForAll0(queue[0].left):
            queue[0].left = None
        else:
            queue.append(queue[0].left)

        if CheckForAll0(queue[0].right):
            queue[0].right = None
        else:
            queue.append(queue[0].right)
        queue.pop(0)

# Checks for a 1 in the subtree at the passed node
# If none exist return True, else False.
def CheckForAll0(node):
    if node is None:
        return True

    if node.right is None and node.left is None:
        if node.val == 0:
            return True
        if node.val == 1:
            return False
    if node.right is not None and node.left is not None:
        if node.right.val == 1 or node.left.val == 1 or node.val == 1:
            return False
    if CheckForAll0(node.right) and CheckForAll0(node.left):
        return True
    return False

in1 = BinaryTree(0, BinaryTree(1, BinaryTree(0, None, None), BinaryTree(0, None, None) ), BinaryTree(0, BinaryTree(1, BinaryTree(0, None, None), BinaryTree(0, None, None)), BinaryTree(0, None, None)))
printBinaryTree(in1)
print()

# Return solution to example given in problem description.
Solution(in1)
printBinaryTree(in1)