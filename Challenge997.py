"""
Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s)
which deserializes the string back into the tree.
"""

class Tree:
    l = None
    r = None
    val = None

    def __init__(self, value, left = None, right = None):
        self.l = left
        self.r = right
        self.val = value

def printBinaryTree(bt):
    layer = 1
    count = 0
    printStr = ""
    queue = []
    queue.append(bt)

    while len(queue) != 0:

        if queue[0] is not None:
            if queue[0].val is not None:
                printStr += "\'" + str(queue[0].val) + "\' "
            else:
                printStr += "_ "
            queue.append(queue[0].l)
            queue.append(queue[0].r)
        else:
            printStr += "_ "

        queue.pop(0)
        count += 1
        if count == layer:
            layer = len(queue)
            count = 0
            print(printStr)
            printStr = ""

def serialize(root):
    if root is None:
        return ""
    l = serialize(root.l)
    r = serialize(root.r)
    return str(root.val) + "(" + l + ")" + "(" + r + ")"
    
def deserialize(ar):
    if ar == "":
        return None
    for i in range(len(ar)):
        if ar[i] == "(":
            break
    retVal = Tree(ar[:i])
    left, right = getSubTreeFromStr(ar, i)
    retVal.l = deserialize(left)
    retVal.r = deserialize(right)
    return retVal

def getSubTreeFromStr(ar, i):
    openBrac = 0
    CloseBrac = 0
    left = ""
    right = ""
    for j in range(i, len(ar)):
        if ar[j] == "(":
            openBrac += 1
        if ar[j] == ")":
            CloseBrac += 1
        
        if openBrac == CloseBrac:
            if left == "":
                left = ar[i: j + 1]
                i = j + 1
                CloseBrac = openBrac = 0
            else:
                right = ar[i: j + 1]
                i = j + 1
                CloseBrac = openBrac = 0
    return left[1:-1], right[1:-1]
    

# serialize Return 4(2(1()())(3()()))(6(5()())(7()()))  | deserialize returns original tree
in1 = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
printBinaryTree(in1)
in2 = serialize(in1)
print(in2)
in3 = deserialize(in2)
printBinaryTree(in3)

print("\n")

# serialize Return 4(2(1()())())(6(5()())(7()()))  | deserialize returns original tree
in1 = Tree(4, Tree(2, Tree(1)), Tree(6, Tree(5), Tree(7)))
printBinaryTree(in1)
in2 = serialize(in1)
print(in2)
in3 = deserialize(in2)
printBinaryTree(in3)

print("\n")

# serialize Return 202(100()())(3333()())  | deserialize returns original tree
in1 = Tree(202, Tree(100), Tree(3333))
printBinaryTree(in1)
in2 = serialize(in1)
print(in2)
in3 = deserialize(in2)
printBinaryTree(in3)

print("\n")

# assert should pass
node = Tree('root', Tree('left', Tree('left.left')), Tree('right'))
assert deserialize(serialize(node)).l.l.val == 'left.left'