"""
Given two singly linked lists that intersect at some point,
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.

In this example, assume nodes with the same
value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists)
and constant space.
"""

class LL:
    val = n = None
    def __init__(self, value, nextVal = None):
        self.val = value
        self.n = nextVal

def printLL(ar):
    retVal = ""
    temp = ar
    while temp is not None:
        retVal += str(temp.val) + " -> "
        temp = temp.n
    retVal += "None"
    print(retVal)

def Solution(ll1, ll2):
    cur1 = ll1
    cur2 = ll2
    
    while cur1.val != cur2.val:
        if cur1.val == cur2.val:
            break
        
        cur1 = cur1.n
        cur2 = cur2.n
        
        if cur1 is None:
            cur1 = ll2
        if cur2 is None:
            cur2 = ll1
    return cur1

# Return 8
in1 = LL(3, LL(7, LL(8, LL(10))))
in2 = LL(99, LL(1, LL(8, LL(10))))
print(Solution(in1, in2).val)

# Return 3
in1 = LL(1, LL(2, LL(3, LL(4, LL(5)))))
in2 = LL(99, LL(89, LL(72, LL(64, LL(51, LL(48, LL(29, LL(11, LL(3, LL(4, LL(5)))))))))))
print(Solution(in1, in2).val)