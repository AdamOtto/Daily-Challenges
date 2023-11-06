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


def Solution(S):
    retVal = Helper(S)
    return retVal

def Helper(cur):
    if len(cur) == 0:
        return None
    if len(cur) == 1:
        return Tree(cur[0])
    minInd = findMinIndex(cur)
    retVal = Tree(cur[minInd])
    retVal.l = Helper(cur[:minInd])
    retVal.r = Helper(cur[minInd + 1:])
    return retVal
    
def findMinIndex(cur):
    min_val = min(cur)
    return cur.index(min_val)



"""
Return:
      1
    /   \   
  2       9
 / \
3   6
"""
S = [3, 2, 6, 1, 9]
t = Solution(S)
printBinaryTree(t)

print()

"""
Return:
          1
       /     \
      2       5
     / \     / \
    4   3   6   7
   / \           \
  10  9           8
"""
S = [10,4,9,2,3,1,6,5,7,8]
t = Solution(S)
printBinaryTree(t)