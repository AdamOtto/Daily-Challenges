"""
Given the sequence of keys visited by a postorder
traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5,
you should construct the following tree:

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
    l = len(ar)

    if l == 1:
        return Tree(ar[0], None, None)
    elif l == 0:
        return None
    root = Tree(ar[l - 1], None, None)
    left = None
    right = None


    for i in reversed(range(0, l - 1)):
        if ar[i] < root.val:
            left = ar[0:i + 1]
            right = ar[i + 1:l-1]
            break
    if left is not None:
        root.l = Solution(left)
        root.r = Solution(right)
    else:
        root.r = Solution(ar[0:l-1])
    return root

# Return example given.
printBinaryTree(Solution([2, 4, 3, 8, 7, 5]))
 
"""
Return:
     40
    /   \
  20     60
 /  \   /  \
10  30 50  70
"""
printBinaryTree(Solution([10, 30, 20, 50, 70, 60, 40]))