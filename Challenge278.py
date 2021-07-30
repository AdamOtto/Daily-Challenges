'''
Given an integer N, construct all possible binary search trees with N nodes.
'''
import itertools

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

def Solution(N):
    retVal = []
    
    temp2 = [x for x in range(1, N + 1)]
    l = list(itertools.permutations(temp2))
    for perm in l:
        temp = Tree(perm[0])
        for elem in perm:
            AddNode(temp, elem)
        addVal = True
        for vals in retVal:
            if treeCompare(vals, temp):
                addVal = False
                break
        if addVal:
            retVal.append(temp)
        
    return retVal


def AddNode(cur, val):
    if cur.val > val:
        if cur.l is None:
            cur.l = Tree(val)
            return
        else:
            AddNode(cur.l, val)
    elif cur.val < val:
        if cur.r is None:
            cur.r = Tree(val)
            return
        else:
            AddNode(cur.r, val)
    return

def treeCompare(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is not None and tree2 is None:
        return False
    if tree1 is None and tree2 is not None: 
        return False
    
    if tree1.val != tree2.val:
        return False
    if not treeCompare(tree1.l, tree2.l):
        return False
    if not treeCompare(tree1.r, tree2.r):
        return False
    return True

N = 3
trees = Solution(N)
print(str(len(trees)) + " trees returned:\n")
for n in trees:
    printBinaryTree(n)
    print()