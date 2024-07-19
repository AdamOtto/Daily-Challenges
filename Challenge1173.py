"""
A Cartesian tree with sequence S is a binary tree defined by the following two properties:

It is heap-ordered, so that each parent value is strictly less than that of its children.
An in-order traversal of the tree produces nodes with values that correspond exactly to S.
For example, given the sequence [3, 2, 6, 1, 9], the resulting Cartesian tree would be:

      1
    /   \   
  2       9
 / \
3   6
Given a sequence S, construct the corresponding Cartesian tree.
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
    if ar is None or len(ar) == 0:
        return None
    if len(ar) == 1:
        return Tree(ar[0])
    head = ar.index(min(ar))
    retVal = Tree(ar[head])
    retVal.l = Solution(ar[0:head])
    retVal.r = Solution(ar[head + 1:])
    return retVal

"""
 Return:
       '1' 
   '2'      '9' 
 '3'  '6'    _ _ 
_ _   _ _ 
"""
printBinaryTree(Solution([3, 2, 6, 1, 9]))

print()
"""
 Return:
           '1' 
      '2'       '7' 
  '4'     '3'   _ _ 
'6' '5'   _ _ 
_ _ _ _ 
"""
printBinaryTree(Solution([6, 4, 5, 2, 3, 1, 7]))