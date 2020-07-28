"""
A unival tree (which stands for "universal value") is a
tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.
"""

class node:
    val = 0
    rn = None
    ln = None
    def __init__(self, value, leftNode = None, RightNode = None):
        self.val = value
        self.rn = RightNode
        self.ln = leftNode

def universalCount(tree):
    c, _ = dig(tree)
    return c
    
def dig(node):
    if node is None:
        return 0, True
        
    lcount, luniv = dig(node.ln)
    rcount, runiv = dig(node.rn)
    tot = lcount + rcount
    
    if luniv and runiv:
        if (node.ln is not None) and (node.val != node.ln.val):
            return tot, False
        elif (node.rn is not None) and (node.val != node.rn.val):
            return tot, False
        else:
            return tot + 1, True
    else:
        return tot, False
    
tree = node(0, node(1), node(0, node(1, node(1),node(1) ), node(0)))
print( universalCount(tree) )