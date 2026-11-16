"""
Given a node in a binary search tree,
return the next bigger element,
also known as the inorder successor

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
   
Ex 2:
               30
            /     \
          15       40
         /  \     /  \
        5    20  35   50
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

def getNextHighest(cur):
    if cur.l is not None:
        return getNextHighest(cur.l)
    return cur.val
    

def Solution(cur, initVal = None):
    if cur is None:
        return None
    if initVal is not None and cur.p is None:
        if initVal < cur.val:
            return cur.val
        else:
            return None
    if initVal is not None:
        if initVal < cur.val:
            return cur.val
        else:
            if cur.r is not None:
                if cur.p.val < cur.r.val or cur.r.val == initVal:
                    return Solution(cur.p, initVal)
                else:
                    return Solution(cur.r, initVal)
            else:
                return Solution(cur.p, initVal)
    else:
        if cur.p is not None:
            return Solution(cur, cur.val)
        else:
            if cur.r is not None:
                return getNextHighest(cur.r)
    
    

# Return 30
in1 = Tree(10, Tree(5), Tree(30, Tree(22), Tree(35)))
SetParents(in1)
print(Solution(in1.r.l))
# Return 22
print(Solution(in1))
# Return None
print(Solution(in1.r.r))

print()

# Return 30
in2 = Tree(30, Tree(15, Tree(5), Tree(20)), Tree(40, Tree(35), Tree(50)))
SetParents(in2)
print(Solution(in2.l.r))
# Return 20
print(Solution(in2.l))
# Return 15
print(Solution(in2.l.l))
# Return None
print(Solution(in2.r.r))