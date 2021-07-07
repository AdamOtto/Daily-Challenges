"""
Given a sorted linked list, rearrange the node values such that they appear
in alternating low -> high -> low -> high ... form.

For example, given 1 -> 2 -> 3 -> 4 -> 5
you could return 1 -> 3 -> 2 -> 5 -> 4 or 1 -> 5 -> 2 -> 4 -> 3.
"""

class LinkedList:
    n = None
    v = None

    def __init__(self, value, nextValue = None):
        self.v = value
        self.n = nextValue

def printLL(ar):
    t = ar
    retVal = ""
    
    while t is not None:
        retVal += str(t.v) + " -> "
        t = t.n
    retVal += "end"
    print(retVal)

def Solution(ar):
    slow = ar
    fast = slow.n
    
    while fast != None and fast.n != None:
        slow = slow.n
        fast = fast.n.n
    
    LowLL = ar
    HighLL = slow.n
    slow.n = None
    HighLL = reverseLL(HighLL)
    
    retVal = LowLL
    cur = retVal
    LowLL = LowLL.n
    while LowLL != None or HighLL != None:
        if HighLL != None:
            cur.n = HighLL
            cur = cur.n
            HighLL = HighLL.n
        if LowLL != None:
            cur.n = LowLL
            cur = cur.n
            LowLL = LowLL.n
    
    return retVal

def reverseLL(ar):
    prev = None
    cur = ar
    next = None
    while cur != None:
        next = cur.n
        cur.n = prev
        prev = cur
        cur = next
    return prev
    

in1 = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
printLL(in1)
in1 = Solution(in1)
printLL(in1)
print()
in1 = LinkedList(100, LinkedList(150, LinkedList(175, LinkedList(225, LinkedList(400, LinkedList(415, LinkedList(450)))))))
printLL(in1)
in1 = Solution(in1)
printLL(in1)