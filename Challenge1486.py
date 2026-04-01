"""
Given a linked list of numbers and a pivot k,
partition the linked list so that all nodes less
than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3,
the solution could be 1 -> 0 -> 5 -> 8 -> 3.
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

def Solution(ar, k):
    prev = ar
    cur = ar
    smallList = None
    smallListRoot = None
    largeListRoot = None
    while cur is not None and cur.val < k:
        prev = cur
        smallList = cur
        if smallListRoot is None:
            smallListRoot = cur
        cur = cur.n
    largeListRoot = cur
    
    while cur is not None:
        if cur.val >= k:
            prev = cur
        else:
            if smallListRoot is None:
                smallListRoot = cur
            if smallList is not None:
                smallList.n = cur
                smallList = smallList.n
            else:
                smallList = cur
            prev.n = cur.n
        cur = cur.n
    if smallList is not None:
        smallList.n = largeListRoot
    else:
        return ar
    return smallListRoot
    
# Return '1 -> 0 -> 5 -> 8 -> 3 -> None'
in1 = LL(5, LL(1, LL(8, LL(0,LL(3)))))
in1 = Solution(in1, 3)
printLL(in1)

# Return '1 -> 0 -> 2 -> 3 -> 5 -> 4 -> 6'
in1 = LL(1, LL(0, LL(2, LL(5,LL(3, LL(4, LL(6)))))))
in1 = Solution(in1, 4)
printLL(in1)

# Return '100 -> 99 -> 98 -> 97 -> 96 -> 95 -> 94 -> None'
in1 = LL(100, LL(99, LL(98, LL(97,LL(96, LL(95, LL(94)))))))
in1 = Solution(in1, 4)
printLL(in1)

# Return '95 -> 94 -> 100 -> 99 -> 97 -> 98 -> 96 -> None'
in1 = LL(100, LL(99, LL(95, LL(97,LL(94, LL(98, LL(96)))))))
in1 = Solution(in1, 96)
printLL(in1)

# Return '100 -> 99 -> 98 -> 97 -> 96 -> 95 -> 94 -> None'
in1 = LL(100, LL(99, LL(98, LL(97,LL(96, LL(95, LL(94)))))))
in1 = Solution(in1, 101)
printLL(in1)