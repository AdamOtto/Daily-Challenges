"""
The horizontal distance of a binary tree node describes how far left
or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:
The horizontal distance of the root is 0.
The horizontal distance of a left child is hd(parent) - 1.
The horizontal distance of a right child is hd(parent) + 1.

For example, for the following tree, hd(1) = -2, and hd(6) = 0.
             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
The bottom view of a tree, then, consists of the lowest node at each horizontal distance.
If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, (4 or 6), 8, 9].

Given the root to a binary tree, return its bottom view.
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
    d = {}
    MeasureTree(ar, d)
    minhd = min(d)
    maxhd = max(d)
    retVal = []
    for i in range(minhd, maxhd + 1):
        if i in d:
            if len(d[i]) > 1:
                temp = d[i][0]
                for j in range(1, len(d[i])):
                    if temp[1] < d[i][j][1]:
                        temp = d[i][j]
                retVal.append(temp[0])
            else:
                retVal.append(d[i][0][0])
                    
    return retVal
    
def MeasureTree(ar, d, hd = 0, height = 0):
    if ar is None:
        return
    if hd not in d:
        d[hd] = []
    d[hd].append( (ar.val, height) )
    
    MeasureTree(ar.l, d, hd - 1, height + 1)
    MeasureTree(ar.r, d, hd + 1, height + 1)
    return

# Return [0, 1, 3, 4, 8, 9]
in1 = Tree(5, Tree(3, Tree(1, Tree(0)), Tree(4)), Tree(7, Tree(6), Tree(9, Tree(8))))
print(Solution(in1))

# Return [1, 2, 3, 6, 7]
in1 = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
print(Solution(in1))

# Return [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]
in1 = Tree(1, Tree(2, Tree(3, Tree(4))), Tree(5, None, Tree(6, None, Tree(7, None, Tree(8, None, Tree(9, None, Tree(10)))))))
print(Solution(in1))