"""
Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 4 -> 5 -> 1 -> 2 -> 3.
"""
class LL:
    val = None
    n = None
    
    def __init__(self, Value, Next = None):
        self.val = Value
        self.n = Next

def printLL(ar):
    retVal = ""
    temp = ar
    while temp is not None:
        retVal += str(temp.val) + " -> "
        temp = temp.n
    retVal += "None"
    print(retVal)

def Solution(ar, k):
    head = ar
    tail = ar
    while tail.n is not None:
        tail = tail.n

    for i in range(k):
        tail.n = head
        temp = head
        head = head.n
        temp.n = None
        tail = tail.n
    
    return head

# Return 3 -> 5 -> 7 -> 7 -> None
in1 = LL(7, LL(7, LL(3, LL(5))))
printLL(Solution(in1, 2))

# Return 4 -> 5 -> 1 -> 2 -> 3 -> None
in1 = LL(1, LL(2, LL(3, LL(4, LL(5)))))
printLL(Solution(in1, 3))

# Return 4 -> 3 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5 -> None
in1 = LL(8, LL(7, LL(6, LL(5, LL(4, LL(3, LL(2, LL(1))))))))
printLL(Solution(in1, 4))