"""
A ternary search tree is a trie-like data structure where each
node may have up to three children. Here is an example which represents
the words code, cob, be, ax, war, and we.

       c
    /  |  \
   b   o   w
 / |   |   |
a  e   d   a
|    / |   | \ 
x   b  e   r  e  
The tree is structured according to the following rules:

left child nodes link to words lexicographically earlier than the parent prefix
right child nodes link to words lexicographically later than the parent prefix
middle child nodes continue the current word
For instance, since code is the first word inserted in the tree,
and cob lexicographically precedes cod, cob is represented as a left child extending from cod.

Implement an insertion functions for a ternary search tree.
"""

class Tree:
    l = None
    m = None
    r = None
    val = None

    def __init__(self, value, left = None, middle = None, right = None):
        self.l = left
        self.m = middle
        self.r = right
        self.val = value

def printTree(bt):
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
            queue.append(queue[0].m)
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

def Insert(ar, word):
    wordHold = list(word)
    cur = ar
    if ar is None:
        retVal = Tree(wordHold[0])
        cur = retVal
        for i in range(1, len(wordHold)):
            n = Tree(wordHold[i])
            cur.m = n
            cur = cur.m
        return retVal
    w = Tree(wordHold.pop(0))
    while len(wordHold) > 0:
        #print(w.val)
        
        if ord(w.val) == ord(cur.val):
            if cur.m is None:
                cur.m = w
                break
            w = Tree(wordHold.pop(0))
            cur = cur.m
        if ord(w.val) < ord(cur.val):
            if cur.l is None:
                cur.l = w
                cur = cur.l
                break
            cur = cur.l
        elif ord(w.val) > ord(cur.val):
            if cur.r is None:
                cur.r = w
                cur = cur.r
                break
            cur = cur.r

    # Put rest of word under
    while len(wordHold) > 0:
        w = Tree(wordHold.pop(0))
        cur.m = w
        cur = cur.m
    
    return ar

t = None
w = "code"
t = Insert(t, w)
#printTree(t)
print()
w = "cob"
t = Insert(t, w)
#printTree(t)
print()
w = "be"
t = Insert(t, w)
#printTree(t)
print()
w = "ax"
t = Insert(t, w)
#printTree(t)
print()
w = "war"
t = Insert(t, w)
#printTree(t)
print()
w = "we"
t = Insert(t, w)
printTree(t)