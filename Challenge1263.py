"""
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
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
    Helper(ar, [], retVal)
    return retVal

def Helper(cur, l, retVal):
    if cur is None:
        return
    temp = []
    if cur.l is None and cur.r is None:
        temp.extend(l)
        temp.append(cur.val)
        retVal.append(temp)
    
    if cur.l is not None:
        temp = []
        temp.extend(l)
        temp.append(cur.val)
        Helper(cur.l, temp, retVal)
    if cur.r is not None:
        temp = []
        temp.extend(l)
        temp.append(cur.val)
        Helper(cur.r, temp, retVal)
    return

# Return [[1, 2], [1, 3, 4], [1, 3, 5]]
in1 = Tree(1, Tree(2), Tree(3, Tree(4), Tree(5)))
print(Solution(in1))
# Return [[4, 2, 1], [4, 2, 3], [4, 6, 5], [4, 6, 7]]
in1 = Tree(4, Tree(2,Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
print(Solution(in1))