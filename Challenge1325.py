"""
Given a sorted array, convert it into
a height-balanced binary search tree.
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
    halfL = int(len(ar) / 2)
    
    retVal = Tree(ar[halfL])
    
    retVal.l = Solution(ar[0:halfL])
    retVal.r = Solution(ar[halfL + 1:len(ar)])
    
    return retVal
"""
Return: 
           '5' 
     '3'         '8' 
   '2' '4'    '7'   '9' 
'1' _  _ _  '6' _   _ _ 
"""
in1 = [1,2,3,4,5,6,7,8,9]
t = Solution(in1)
printBinaryTree(t)

print()
"""
             '20' 
      '12'           '101' 
  '10'   '15'    '100'  '132' 
'1' _  '14' _   '40' _   _ _ 
"""
in1 = [1, 10,12,14,15,20,40,100,101,132]
t = Solution(in1)
printBinaryTree(t)