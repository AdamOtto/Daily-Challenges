"""
Given the root to a binary search tree,
find the second largest node in the tree.
"""

class Tree:
    l = None
    r = None
    val = None

    def __init__(self, value, left = None, right = None):
        self.l = left
        self.r = right
        self.val = value

def Solution(ar, cur = [0]):
    if ar is None or cur[0] > 2:
        return
    t = ar.val
    Solution(ar.r, cur)
    cur[0] += 1
    if cur[0] == 2:
        print("Second Largest is:", ar.val)
        return
    
    Solution(ar.l, cur)

# Return 20
in1 = Tree(10, Tree(5), Tree(20, None, Tree(30)))
Solution(in1, [0])

# Return 5
in1 = Tree(10, Tree(5), None)
Solution(in1, [0])

# Return 30
in1 = Tree(25, Tree(10, Tree(5), Tree(15)), Tree(30, Tree(20), Tree(35)))
Solution(in1, [0])