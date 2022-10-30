"""
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""

class LL:
    n = None
    val = None
    prev = None
    def __init__(self, Value, NextVal = None):
        self.n = NextVal
        self.val = Value
        self.prev = None

def printLL(ll):
    t = ll
    s = ""
    while t.n is not None:
        s += str(t.val) + " -> "
        t = t.n
    s += str(t.val)
    print(s)

def SetPrev(ar):
    t1 = ar.n
    t2 = ar
    while t1.n is not None:
        t1.prev = t2
        t1 = t1.n
        t2 = t2
    t1.prev = t2
    return

def Solution(ar):
    first = ar
    last = ar
    while last.n is not None:
        last = last.n
    while first.val == last.val:
        first = first.n
        last = last.prev
    
    if last == ar:
        return True
    return False

# Return False
in1 = LL(1, LL(2, LL(3,LL(4))))
printLL(in1)
SetPrev(in1)
print(Solution(in1))

# Return True
in1 = LL(1, LL(2, LL(2,LL(1))))
printLL(in1)
SetPrev(in1)
print(Solution(in1))

# Return True
in1 = LL(1, LL(2, LL(3,LL(2,LL(1)))))
printLL(in1)
SetPrev(in1)
print(Solution(in1))