"""
Given a linked list and a positive integer k, rotate the list to the right by k places.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
"""


class LinkedList:
    val = None
    next = None

    def __init__(self, value, nextNode = None):
        self.val = value
        self.next = nextNode

    def printLinkedList(self):
        k = self.next
        retVal = str(self.val) + " -> "
        while k.next is not None:
            retVal += str(k.val) + " -> "
            k = k.next
        retVal += str(k.val)
        print(retVal)


def Solution(ll, k):
    count = 1
    end = ll
    swap = ll
    while end.next is not None:
        end = end.next
        if count < k - 1:
            swap = swap.next
        count += 1
    end.next = ll
    t = swap.next
    swap.next = None
    return t



in1 = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
k = 3
in1.printLinkedList()
in1 = Solution(in1, k)
in1.printLinkedList()
