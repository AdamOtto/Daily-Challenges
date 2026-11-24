"""
Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right,
and satisfies the constraint that the key in the left child must
be less than or equal to the root and the key in the right child
must be greater than or equal to the root.
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
    if ar.l is None and ar.r is None:
        return True
    if ar.l is None and ar.r is not None:
        if ar.r.val >= ar.val:
            return Solution(ar.r)
        else:
            return False
    
    if ar.l is not None and ar.r is None:
        if ar.l.val <= ar.val:
            return Solution(ar.l)
        else: return False

    if ar.l.val <= ar.val and ar.r.val >= ar.val:
        return Solution(ar.l) and Solution(ar.r)
    else:
        return False

# Return True
print(Solution(Tree(2, Tree(1), Tree(3))))
# Return False
print(Solution(Tree(3, Tree(1), Tree(2))))
# Return True
print(Solution(Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))))