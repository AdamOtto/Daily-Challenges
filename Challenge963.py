"""
Given two singly linked lists that intersect at some point,
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10
and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""
class LL:
    n = None
    val = None
    
    def __init__(self, Value, Next = None):
        self.n = Next
        self.val = Value
    def getLength(self):
        if self.n is not None:
            return 1 + self.n.getLength()
        return 1

def Solution(ar1, ar2):
    l1 = ar1.getLength()
    l2 = ar2.getLength()
    while l1 > 0 and l2 > 0:
        t1 = ar1.val
        t2 = ar2.val
        if ar1.val == ar2.val:
            return ar1.val
        if l1 > l2:
            ar1 = ar1.n
            l1 -= 1
        elif l1 < l2:
            ar2 = ar2.n
            l2 -= 1
        else:
            ar1 = ar1.n
            l1 -= 1
            ar2 = ar2.n
            l2 -= 1
    return None

# Return 8
A = LL(3, LL(7, LL(8, LL(10))))
B = LL(99, LL(1, LL(8, LL(10))))
#print(Solution(A, B))

# Return None
A = LL(1, LL(2, LL(3, LL(4, LL(5, LL(6))))))
B = LL(10, LL(9, LL(8, LL(7, LL(6, LL(5, LL(4, LL(3, LL(2, LL(1))))))))))
#print(Solution(A, B))

# Return 3
A = LL(1, LL(2, LL(3, LL(4, LL(5, LL(6))))))
B = LL(10, LL(9, LL(8, LL(7, LL(6, LL(5, LL(4, LL(3, LL(2, LL(1, LL(0)))))))))))
print(Solution(A, B))