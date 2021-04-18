"""
Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8

"""

class Tree:
    l = None
    r = None
    val = None

    def __init__(self, Value, Left, Right):
        self.val = Value
        self.r = Right
        self.l = Left

def Solution(in1):
    l = len(in1)

    if l == 1:
        return Tree(in1[0], None, None)
    elif l == 0:
        return None
    root = Tree(in1[l - 1], None, None)
    left = None
    right = None


    for i in reversed(range(0, l - 1)):
        if in1[i] < root.val:
            left = in1[0:i + 1]
            right = in1[i + 1:l-1]
            break
    # print("Left: " + str(left))
    # print("Right: " + str(right))
    if left is not None:
        root.l = Solution(left)
        root.r = Solution(right)
    else:
        root.r = Solution(in1[0:l-1])
    return root

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

#in1 = [2,4,3,8,7,5]
in1 = [40,85,80,95,90,135,105,120,130,125,100]
t = Solution(in1)
printBinaryTree(t)