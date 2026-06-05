"""
In Ancient Greece, it was common to write text with the first
line going left to right, the second line going right to left,
and continuing to go back and forth. This style was called "boustrophedon".
Given a binary tree, write an algorithm to
print the nodes in boustrophedon order.
For example, given the following tree:
       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].
"""
class Tree:
    l = None
    r = None
    val = None

    def __init__(self, value, left = None, right = None):
        self.l = left
        self.r = right
        self.val = value

def Solution(ar):
    retVal = []
    retVal.append(ar.val)
    readR2L = True
    nextLayer = []
    tempnextLayer = []
    
    nextLayer.append(ar.l)
    nextLayer.append(ar.r)
    
    while len(nextLayer) > 0:
        for i in range(len(nextLayer)):
            if nextLayer[i].l is not None:
                tempnextLayer.append(nextLayer[i].l)
            if nextLayer[i].r is not None:
                tempnextLayer.append(nextLayer[i].r)
        
        if readR2L:
            for i in reversed(range(len(nextLayer))):
                retVal.append(nextLayer[i].val)
            readR2L = False
        else:
            for i in range(len(nextLayer)):
                retVal.append(nextLayer[i].val)
            readR2L = True
        nextLayer = tempnextLayer
        tempnextLayer = []
    
    return retVal

# Return [1, 3, 2, 4, 5, 6, 7]
in1 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
print(Solution(in1))

# Return [100, 150, 50, 25, 75, 125, 175, 187, 162, 136, 112, 87, 62, 36, 12]
in1 = Tree(100, Tree(50, Tree(25,Tree(12), Tree(36)), Tree(75, Tree(62), Tree(87))), Tree(150, Tree(125, Tree(112), Tree(136)), Tree(175, Tree(162), Tree(187))))
print(Solution(in1))