"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """
class Tree:
    l = None
    r = None
    val = None

    def __init__(self, value, left = None, right = None):
        self.l = left
        self.r = right
        self.val = value
 
def Solution(tree):
    c, _ = dig(tree)
    return c
    
def dig(node):
    if node is None:
        return 0, True
        
    lcount, luniv = dig(node.l)
    rcount, runiv = dig(node.r)
    tot = lcount + rcount
    
    if luniv and runiv:
        if (node.l is not None) and (node.val != node.l.val):
            return tot, False
        elif (node.r is not None) and (node.val != node.r.val):
            return tot, False
        else:
            return tot + 1, True
    else:
        return tot, False

# Return 5
in1 = Tree(0, Tree(1), Tree(0, Tree(1, Tree(1), Tree(1)), Tree(0)))
print(Solution(in1))

# Return 4
in1 = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
print(Solution(in1))