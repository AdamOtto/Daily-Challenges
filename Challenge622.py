"""
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
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
    q = []
    q.append( (ar, 0) )
    deepestLevel = 0
    retVal = ""
    
    while len(q) > 0:
        node, level = q.pop(0)
        if node is not None:
            if level > deepestLevel:
                deepestLevel = level
                retVal = node.val
            q.append( (node.l, level + 1 ) )
            q.append( (node.r, level + 1 ) )
    return retVal

# Return d
in1 = Tree("a", Tree("b", Tree("d")), Tree("c"))
print(Solution(in1))

# Return 1 or 3 or 5 or 7
in1 = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
print(Solution(in1))