"""
Huffman coding is a method of encoding characters based on their frequency.
Each letter is assigned a variable-length binary string, such as 0101 or 111110,
where shorter lengths correspond to more common letters.
To accomplish this, a binary tree is built such that the path from the root to
any leaf uniquely maps to a character. When traversing the path,
descending to a left child corresponds to a 0 in the prefix,
while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree,
and use it to determine a mapping between characters and their encoded binary strings.
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

def Solution_BuildHuffmanTree(ar):
    l = len(ar)
    minStackNodes = []
    for key, val in ar.items():
        minStackNodes.append( (Tree(key), val) )
    minStackNodes.sort(key = lambda x:x[1])
    #print(minStackNodes)

    while len(minStackNodes) > 1:
        t1 = minStackNodes.pop(0)
        t2 = minStackNodes.pop(0)

        newNode = Tree(None)
        newNode.l = t1[0]
        newNode.r = t2[0]
        minStackNodes.append( (newNode, t1[1] + t2[1]) )
        minStackNodes.sort(key=lambda x: x[1])
    return minStackNodes[0][0]

def Solution_FindEncodingString(ar, encStr):
    d = {}
    retVal = ""
    Helper(ar.l, d, "0")
    Helper(ar.r, d, "1")

    for char in encStr:
        retVal += d[char]

    return retVal


def Helper(ar, d, curStr):
    if ar is None:
        return
    if ar.val is not None:
        d[ar.val] = curStr
        return

    Helper(ar.l, d, curStr + "0")
    Helper(ar.r, d, curStr + "1")
    return

in1 = {'c' : 1, 'a' : 1, 't' : 1, 's' : 1}
t = Solution_BuildHuffmanTree(in1)
printBinaryTree(t)
print(Solution_FindEncodingString(t, "cats"))

print("\n")

s = "helloworld"
in1 = {}
for char in s:
    if char not in in1:
        in1[char] = 1
    else:
        in1[char] += 1
t = Solution_BuildHuffmanTree(in1)
printBinaryTree(t)
print(Solution_FindEncodingString(t, s))

print("\n")

s = "this is a test.  this is also a t-t-t-test. test.  test test."
in1 = {}
for char in s:
    if char not in in1:
        in1[char] = 1
    else:
        in1[char] += 1
t = Solution_BuildHuffmanTree(in1)
printBinaryTree(t)
print(Solution_FindEncodingString(t, s))

print("\n")

s = "everyone likes me said caul shivers the most feared man in the north"
in1 = {}
for char in s:
    if char not in in1:
        in1[char] = 1
    else:
        in1[char] += 1
t = Solution_BuildHuffmanTree(in1)
printBinaryTree(t)
print(Solution_FindEncodingString(t, s))