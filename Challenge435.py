"""
Given pre-order and in-order traversals of a binary tree,
write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
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


def buildTree(ar1, ar2):
    if ar2 is None or len(ar2) == 0:
        return None
    
    if len(ar2) % 2 >= 1:
        mid = int(len(ar2) / 2)
    else:
        mid = getMid(ar1, ar2)
    retVal = Tree(ar2[mid])
    retVal.l = buildTree(ar1, ar2[0:mid])
    retVal.r = buildTree(ar1, ar2[mid + 1:])
    return retVal
    
def getMid(ar1, ar):
    for i in range(0, len(ar1)):
        if ar1[i] in ar:
            return ar.index(ar1[i])
    return None

# Return results given in example
printBinaryTree(buildTree(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g']))

# Return 
#       '4' 
#   '2'      '6' 
#'1'  '3'  '5'  _ 
printBinaryTree(buildTree([4,2,1,3,6,5], [1,2,3,4,5,6]))

# Return 
#       '4' 
#   '2'      '6' 
#'1'  '3'  '5' '7' 
printBinaryTree(buildTree([4,2,1,3,6,5,7], [1,2,3,4,5,6,7]))