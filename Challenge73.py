'''
Given the head of a singly linked list, reverse it in-place
'''

class llist:
    val = 0
    nextn = None
    def __init__(self, value, nextNode):
        self.val = value
        self.nextn = nextNode
        
def printllist(ll):
    t = ll
    out = ""
    while t.nextn != None:
        out += str(t.val) + " "
        t = t.nextn
    out += str(t.val)
    print(out)


def Solution(ll):
    prev = ll
    cur = ll.nextn
    nextNode = None
    
    prev.nextn = None
    
    while cur != None:
        nextNode = cur.nextn
        cur.nextn = prev
        prev = cur
        cur = nextNode
    ll = prev
    return prev
    
    
    

in1 = llist(0, None)
t = in1
for i in range(1, 11):
    t.nextn = llist(i, None)
    t = t.nextn
printllist(in1)
in1 = Solution(in1)
printllist(in1)