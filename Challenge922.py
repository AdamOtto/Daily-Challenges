"""
Implement locking in a binary tree.
A binary tree node can be locked or unlocked only if all
of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

 - is_locked, which returns whether the node is locked
 - lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
 - unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any
other property you would like. You may assume the class is used in a single-threaded program,
so there is no need for actual locks or mutexes.
Each method should run in O(h), where h is the height of the tree.
"""

class Tree:
    l = None
    r = None
    val = None
    locked = None
    
    def __init__(self, value, left = None, right = None):
        self.l = left
        self.r = right
        self.val = value
        self.locked = False
    
    def is_locked(self):
        return self.locked
    

def printBinaryTree(bt):
    layer = 1
    count = 0
    printStr = ""
    queue = []
    queue.append(bt)

    while len(queue) != 0:

        if queue[0] is not None:
            if queue[0].val is not None:
                if queue[0].locked:
                    printStr += "\'" + str(queue[0].val) + "X" + "\' "
                else:
                    printStr += "\'" + str(queue[0].val) + "O" + "\' "
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

def lock(tree, cur):
    if tree.val == cur.val:
        if checkDescendants(tree.l) and checkDescendants(tree.r) and not tree.locked:
            tree.locked = True
            return tree.locked
        else:
            return False
    else:
        if tree.locked:
            return False
        if cur.val > tree.val:
            return lock(tree.r, cur)
        else:
            return lock(tree.l, cur)

def checkDescendants(tree):
    if tree is None:
        return True
    if tree.locked:
        return False
    
    if checkDescendants(tree.l):
        if checkDescendants(tree.r):
            return True
    return False
        
def unlock(tree, cur):
    if tree.val == cur.val:
        if checkDescendants(tree.l) and checkDescendants(tree.r) and tree.locked:
            tree.locked = False
            return not tree.locked
        else:
            return False
    else:
        if tree.locked:
            return False
        if cur.val > tree.val:
            return unlock(tree.r, cur)
        else:
            return unlock(tree.l, cur)

in1 = Tree(4,Tree(2,Tree(1), Tree(3)), Tree(6,  Tree(5), Tree(7)))
printBinaryTree(in1)

# Return False
print("is head of tree locked:")
print(in1.is_locked())

# Return True
print("Lock tree head:")
print(lock(in1, in1))

# Return False
print("Lock tree head again:")
print(lock(in1, in1))

# Return False
print("Fail to lock right node of tree head:")
temp = in1.r
print(lock(in1, temp))
printBinaryTree(in1)

# Return True
print("Unlock tree head:")
print(unlock(in1, in1))
printBinaryTree(in1)

# Return True
print("Lock right node of tree head:")
print(lock(in1, temp))
printBinaryTree(in1)

# Return False
print("Fail to lock tree head")
print(lock(in1, in1))
printBinaryTree(in1)

# Return True
print("Unlock right node of tree head:")
print(unlock(in1, temp))
printBinaryTree(in1)