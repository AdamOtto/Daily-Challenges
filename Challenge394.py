"""
Given a binary tree and an integer k,
return whether there exists a root-to-leaf path that sums up to k.

For example, given k = 18 and the following binary tree:

    8
   / \
  4   13
 / \   \
2   6   19
Return True since the path 8 -> 4 -> 6 sums to 18.
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

def Solution(ar, k):
    return Helper(ar, 0, k)

def Helper(cur, val, k):
    if cur is None:
        return False
    
    if cur.val + val == k:
        return True
    elif cur.val + val > k:
        return False
    
    if Helper(cur.l, cur.val + val, k) or Helper(cur.r, cur.val + val, k):
        return True
    return False

in1 = Tree(8, Tree(4, Tree(2), Tree(6)), Tree(13, None, Tree(19)))
# Return True
print(Solution(in1, 18))
# Return False
print(Solution(in1, 101))
# Return True
print(Solution(in1, 40))
#printBinaryTree(in1)