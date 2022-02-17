"""
Given the head of a singly linked list, reverse it in-place.
"""

class llist:
    val = 0
    n = None
    def __init__(self, value, node):
        self.val = value
        self.n = node
        
def printllist(ll):
    t = ll
    out = ""
    while t.n != None:
        out += str(t.val) + " "
        t = t.n
    out += str(t.val)
    print(out)


def Solution(ll):
    prev = ll
    cur = ll.n
    node = None
    
    prev.n = None
    
    while cur != None:
        node = cur.n
        cur.n = prev
        prev = cur
        cur = node
    ll = prev
    return prev
    
    
    

in1 = llist(0, None)
t = in1
for i in range(1, 11):
    t.n = llist(i, None)
    t = t.n
printllist(in1)
in1 = Solution(in1)
printllist(in1)