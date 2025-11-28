"""
Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

     *
   /   \
  +     +
 / \   / \
3   2 4   5
You should return 45, as it is (3 + 2) * (4 + 5).
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
    if type(ar.val) is int:
        return ar.val
    elif type(ar.val) is str:
        if ar.val == "*":
            return Solution(ar.l) * Solution(ar.r)
        elif ar.val == "+":
            return Solution(ar.l) + Solution(ar.r)
        elif ar.val == "-":
            return Solution(ar.l) - Solution(ar.r)
        elif ar.val == "/":
            return Solution(ar.l) / Solution(ar.r)
        else:
            return None
    return None
    
# Return 45
in1 = Tree("*", Tree("+", Tree(3), Tree(2)), Tree("+", Tree(4), Tree(5)))
print(Solution(in1))

# Return 25.0
in1 = Tree("*", Tree("/", Tree("+", Tree(15), Tree(5)), Tree(4)), Tree("-", Tree(15), Tree(10)))
print(Solution(in1))
