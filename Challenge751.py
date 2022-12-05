"""
Typically, an implementation of in-order traversal of a
binary tree has O(h) space complexity, where h is the height of the tree.
Write a program to compute the in-order
traversal of a binary tree using O(1) space.
"""
class Tree:
    val = 0
    l = None
    r = None
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.l = left
        self.r = right


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
            
            
def PostOrderTraversal(ar):
    newTree = ar
    dTreeHeight = {}
    dTreeHeight[ar] = 0
    Helper(newTree, dTreeHeight, 0)
    return newTree

def Helper(ar, d, level):
    if ar.l is not None and ar.r is not None:
        if (ar.l in d and d[ar.l] > d[ar]) or ar.l not in d:
            PostOrderMakerLeftSubTree(ar, ar.l, d, level)
            Helper(ar.l, d, level + 1)
        if (ar.r in d and d[ar.r] > d[ar]) or ar.r not in d:
            PostOrderMakerRightSubTree(ar, ar.r, d, level)
            Helper(ar.r, d, level + 1)
    elif ar.l is not None and ar.r is None:
        if (ar.l in d and d[ar.l] > d[ar]) or ar.l not in d:
            PostOrderMakerLeftSubTree(ar, ar.l, d, level)
            Helper(ar.l, d, level + 1)
    elif ar.l is None and ar.r is not None:
        if (ar.r in d and d[ar.r] > d[ar]) or ar.r not in d:
            PostOrderMakerRightSubTree(ar, ar.r, d, level)
            Helper(ar.r, d, level + 1)
    return

def PostOrderMakerRightSubTree(parent, ar, dTreeHeight, level):
    if ar not in dTreeHeight:
        dTreeHeight[ar] = level
        
    if ar.l is None:
        ar.l = parent
    elif ar.l in dTreeHeight:
        if dTreeHeight[ar.l] < dTreeHeight[ar]:
            return
        else:
            PostOrderMakerRightSubTree(parent, ar.l, dTreeHeight, level + 1)
    else:
        PostOrderMakerRightSubTree(parent, ar.l, dTreeHeight, level + 1)
    return

def PostOrderMakerLeftSubTree(parent, ar, dTreeHeight, level):
    if ar not in dTreeHeight:
        dTreeHeight[ar] = level
        
    if ar.r is None:
        ar.r = parent
    elif ar.r in dTreeHeight:
        if dTreeHeight[ar.r] < dTreeHeight[ar]:
            return
        else:
            PostOrderMakerLeftSubTree(parent, ar.r, dTreeHeight, level + 1)
    else:
        PostOrderMakerLeftSubTree(parent, ar.r, dTreeHeight, level + 1)
    return

def TraverseTreeO1(ar):
    retVal = ""
    
    #Traverse left side of root
    cur = ar.l
    goRight = True
    tempString = ""
    while True:
        if goRight:
            if cur.r.val != ar.val:
                cur = cur.r
            else:
                tempString += str(cur.val)
                cur = cur.l
                goRight = False
        else:
            if cur.l is not None:
                tempString += str(cur.val)
                cur = cur.l
            else:
                tempString += str(cur.val)
                break
    retVal += tempString[::-1]
    # Traverse right side of root
    cur = ar.r
    goRight = False
    tempString = ""
    while True:
        if not goRight:
            if cur.l.val != ar.val:
                cur = cur.l
            else:
                tempString += str(cur.val)
                cur = cur.r
                goRight = True
        else:
            if cur.r is not None:
                tempString += str(cur.val)
                cur = cur.r
            else:
                tempString += str(cur.val)
                break

    retVal += str(ar.val) + tempString
    print(retVal)

# Return 428591637
in1 = Tree(1, Tree(2, Tree(4), Tree(5, Tree(8), Tree(9))), Tree(3, Tree(6), Tree(7)))
printBinaryTree(in1)
t = PostOrderTraversal(in1)
TraverseTreeO1(t)