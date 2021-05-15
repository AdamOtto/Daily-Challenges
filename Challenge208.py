"""
Given a linked list of numbers and a pivot k,
partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3,
the solution could be 1 -> 0 -> 5 -> 8 -> 3.
"""

class LinkedList:
    val = None
    next = None

    def __init__(self, CurrentValue, NextValue = None):
        self.val = CurrentValue
        self.next = NextValue

def printLinkedList(top):
    temp = top
    s = ""
    while temp.next is not None:
        s += str(temp.val) + " -> "
        temp = temp.next
    s += str(temp.val)
    print(s)

def Solution(top, k):
    append = None
    appendTrav = None
    temp = top
    last = None
    while temp.next is not None:
        if temp.val < k:
            # Append value to the append LL
            if append is None:
                append = LinkedList(temp.val)
                appendTrav = append
            else:
                appendTrav.next = LinkedList(temp.val)
                appendTrav = appendTrav.next

            # Remove element from list.
            if last is None or temp == top:
                top = top.next
                temp.next = None
                temp = top
                last = temp
            else:
                tempNext = temp.next
                temp.next = None
                last.next = tempNext
                temp = last
        else:
            last = temp
            temp = temp.next

    if temp.val < k:
        appendTrav.next = LinkedList(temp.val)
        appendTrav = appendTrav.next
        last.next = None

    if appendTrav is None:
        return top
    if temp != top:
        appendTrav.next = top
    return append


"""
in1 = LinkedList(5, LinkedList(1, LinkedList(8, LinkedList(0, LinkedList(3)))))
k = 3
printLinkedList(in1)
t = Solution(in1, k)
printLinkedList(t)
"""

in1 = LinkedList(8, LinkedList(7, LinkedList(6, LinkedList(5, LinkedList(4, LinkedList(3, LinkedList(2, LinkedList(1))))))))
k = 5
printLinkedList(in1)
t = Solution(in1, k)
printLinkedList(t)