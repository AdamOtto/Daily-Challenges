"""
Given the root of a binary tree, find the most frequent subtree sum.
The subtree sum of a node is the sum of all values under a node,
including the node itself.
"""

class Tree:
    val = None
    l = None
    r = None

    def __init__(self, value, left = None, right = None):
        self.val = value
        self.l = left
        self.r = right

# O(n^2)
def Solution(t):
    d = {}
    q = []
    q.append(t)

    while len(q) != 0:
        cur = q.pop(0)
        t = getSubTreeSum(cur)
        if t in d:
            d[t] += 1
        else:
            d[t] = 1

        if cur.l is not None:
            q.append(cur.l)
        if cur.r is not None:
            q.append(cur.r)

    max = 0
    for key, val in d.items():
        if val > max:
            max = val
    return max

def getSubTreeSum(t):
    if t.l is not None and t.r is not None:
        return t.val + getSubTreeSum(t.l) + getSubTreeSum(t.r)
    elif t.l is not None and t.r is None:
        return t.val + getSubTreeSum(t.l)
    elif t.l is None and t.r is not None:
        return t.val + getSubTreeSum(t.r)
    return t.val


in1 = Tree(5, Tree(2), Tree(-5))
print(Solution(in1))
