"""
Let's represent an integer in a linked list format
by having each node represent a digit in the number.
The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format,
return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""
class linkedList:
    node = None
    val = None
    def __init__(self, value):
        self.val = value
        self.node = None
        
def MakeLL(n):
    numStr = str(n)
    retVal = linkedList(None)
    t = retVal
    for i in reversed(range(0, len(numStr))):
        t.val = int(numStr[i])
        if i != 0:
            t.node = linkedList(None)
            t = t.node
    t.val = int(numStr[0])
    return retVal

def printLL(n):
    s = ""
    s += str(n.val)
    while n.node is not None:
        n = n.node
        s += "->" + str(n.val)
    print(s)

def sumLL(m, n):
    pointM = m
    pointN = n
    retVal = 0
    i = 1
    while pointN is not None or pointM is not None:
        x = 0
        y = 0
        if pointN is not None:
            x = int(pointN.val)
            pointN = pointN.node
        if pointM is not None:
            y = int(pointM.val)
            pointM = pointM.node
        
        retVal += i * (x + y)
        i = i * 10
        
    return MakeLL(retVal)

# Return 4->2->1
in1 = 99
in2 = 25
t = sumLL(MakeLL(in1), MakeLL(in2))
printLL(t)

# Return 1->1->1->1->1
in1 = 4819
in2 = 6292
t = sumLL(MakeLL(in1), MakeLL(in2))
printLL(t)

# Return 3 -> 3
in1 = 11
in2 = 22
t = sumLL(MakeLL(in1), MakeLL(in2))
printLL(t)