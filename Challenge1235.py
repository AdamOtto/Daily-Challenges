"""
Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(ar):
    if ar is None:
        return ""
    retVal = str(ar.val)
    l = "(" + serialize(ar.left) + ")"
    if l != "()":
        retVal = l + retVal
    r = "(" + serialize(ar.right) + ")"
    if r != "()":
        retVal = retVal + r
    return retVal

def deserialize(ar):
    if ar == "":
        return None
    l = FindParenthesisPair(ar, "Left")
    r = FindParenthesisPair(ar, "Right")
    retVal = Node(ar[l[1] + 1:r[0]])
    #print("Processed", retVal.val)
    if l[1] != -1:
        retVal.left = deserialize(ar[l[0] + 1: l[1]])
    if r[0] != len(ar):
        retVal.right = deserialize(ar[r[0] + 1: r[1]])
    
    return retVal

def FindParenthesisPair(ar, LeftOrRight = None):
    openPar = 0
    closePar = 0
    i = -1
    j = -1
    if LeftOrRight == "Left":
        for i in range(0, len(ar)):
            if ar[i] == "(":
                openPar += 1
                break
        if openPar == 0:
            return (-1, -1)
        j = i
        while j < len(ar) and openPar > closePar:
            j += 1
            if ar[j] == "(":
                openPar += 1
            elif ar[j] == ")":
                closePar += 1
    elif LeftOrRight == "Right":
        for j in reversed(range(0, len(ar))):
            if ar[i] == ")":
                closePar += 1
                break
        if closePar == 0:
            return (len(ar), len(ar))
        i = j
        while i < len(ar) and openPar < closePar:
            i -= 1
            if ar[i] == "(":
                openPar += 1
            elif ar[i] == ")":
                closePar += 1
    return (i, j)

# Expected result: AssertionError is not raised
# Print ((left.left)left)root(right)
node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
assert deserialize(serialize(node)).left.left.val == 'left.left'