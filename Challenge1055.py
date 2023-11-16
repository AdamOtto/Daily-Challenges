"""
Given a node in a binary search tree,
return the next bigger element,
also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.
"""

class Tree:
    p = l = r = val = None
    
    def __init__(self, Value, Left = None, Right = None, Parent = None):
        self.p = Parent
        self.l = Left
        self.r = Right
        self.val = Value

def SetParents(cur, Parent = None):
    if cur is not None:
        cur.p = Parent
        SetParents(cur.l, cur)
        SetParents(cur.r, cur)

def Solution(cur, initVal = None):
    if cur is None:
        return None
    if initVal is not None:
        if initVal < cur.val:
            return cur.val
        else:
            return Solution(cur.p, initVal)
    else:
        return Solution(cur.p, cur.val)

# Return 30
in1 = Tree(10, Tree(2), Tree(30, Tree(22), Tree(35)))
SetParents(in1)
print(Solution(in1.r.l))

# Return None
in1 = Tree(10, Tree(2), Tree(30, Tree(22), Tree(35)))
SetParents(in1)
print(Solution(in1.r.r))

# Return 10
in1 = Tree(10, Tree(2), Tree(30, Tree(22), Tree(35)))
SetParents(in1)
print(Solution(in1.l))