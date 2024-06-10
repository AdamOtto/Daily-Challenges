"""
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""
class LL:
    n = None
    val = None
    def __init__(self, Value, NextVal = None):
        self.n = NextVal
        self.val = Value

def printLL(ll):
    t = ll
    s = ""
    while t.n is not None:
        s += str(t.val) + " -> "
        t = t.n
    s += str(t.val)
    print(s)

def Solution(ar):
    t = ar
    stack = []
    
    while t != None:
        stack.append(t.val)
        t = t.n
    t = ar
    while t != None:
        i = stack.pop()
        if t.val != i:
            return False
        t = t.n
    return True

# Return False
in1 = LL(1, LL(2, LL(3,LL(4))))
printLL(in1)
print(Solution(in1))

# Return True
in1 = LL(1, LL(2, LL(2,LL(1))))
printLL(in1)
print(Solution(in1))

# Return True
in1 = LL(1, LL(2, LL(3, LL(2, LL(1)))))
printLL(in1)
print(Solution(in1))