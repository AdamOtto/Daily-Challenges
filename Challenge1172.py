"""
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

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

def Solution(preOrdTrav, InOrdTrav):
    i = InOrdTrav.index(preOrdTrav[0])
    
    retVal = Tree(InOrdTrav[i])
    cur = [1]
    retVal.l = BuildTree(preOrdTrav, InOrdTrav[0:i], cur)
    retVal.r = BuildTree(preOrdTrav, InOrdTrav[i + 1:], cur)
    return retVal
    

def BuildTree(preOrdTrav, InOrdTrav, cur):
    if len(InOrdTrav) == 0:
        return None
    i = InOrdTrav.index(preOrdTrav[cur[0]])
    t = Tree(InOrdTrav[i])
    cur[0] += 1
    if len(InOrdTrav) <= 1:
        return t
    t.l = BuildTree(preOrdTrav, InOrdTrav[0:i], cur)
    
    if cur[0] < len(preOrdTrav):
        t.r = BuildTree(preOrdTrav, InOrdTrav[i + 1:], cur)
    return t

"""
Return 
      'a' 
  'b'     'c' 
'd' 'e' 'f' 'g' 
_ _ _ _ _ _ _ _ 
"""
printBinaryTree(Solution(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g']))

print()

"""
Return 
       '1' 
   '2'     '3' 
 '4' _     _ '6' 
_ _           _ _
"""
printBinaryTree(Solution(['1', '2', '4', '3', '6'], ['4', '2', '1', '3', '6']))