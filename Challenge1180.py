"""
Given the head of a singly linked list,
swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""
class LinkedList:
    val = None
    next = None

    def __init__(self, value, nextNode = None):
        self.val = value
        self.next = nextNode

def printLL(ll):
    t = ll
    s = ""
    while t.next is not None:
        s += str(t.val) + " -> "
        t = t.next
    s += str(t.val)
    print(s)

def Solution(ll):
    t = ll

    while t is not None and t.next is not None:
        if t.val == t.next.val:
            t = t.next.next
        else:
            t.val, t.next.val = t.next.val, t.val
            t = t.next.next

# Return 2 -> 1 -> 4 -> 3
in1 = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4))))
Solution(in1)
printLL(in1)

# Return 2 -> 1 -> 4 -> 3 -> 5
in1 = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
Solution(in1)
printLL(in1)

# Return 2 -> 1 -> 4 -> 3 -> 6 -> 5
in1 = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5, LinkedList(6))))))
Solution(in1)
printLL(in1)