"""
Given a linked list, sort it in O(n log n) time

For example, the linked list 4 -> 1 -> -3 -> 99
should become -3 -> 1 -> 4 -> 99.
"""

class Node:
    val = None
    n = None
    def __init__(self, data, nextNode = None):
        self.val = data
        self.n = nextNode

def printLL(head):
    retVal = ""
    t = head
    while t is not None:
        retVal += str(t.val) + " -> "
        t = t.n
    retVal += "None"
    print(retVal)

def getMiddle(head):
        if (head == None):
            return head
        slow = head
        fast = head
        while (fast.n != None and fast.n.n != None):
            slow = slow.n
            fast = fast.n.n
        return slow

# O(n logn)
def Solution(ar):
    if ar is None or ar.n is None:
        return ar
    middle = getMiddle(ar)
    nextMiddle = middle.n
    middle.n = None
    left = Solution(ar)
    right = Solution(nextMiddle)
    
    sortedLL = mergeSort(left, right)
    return sortedLL

def mergeSort(left, right):
    retVal = None
    if left is None:
        return right
    if right is None:
        return left
    
    if left.val <= right.val:
        retVal = left
        retVal.n = mergeSort(left.n, right)
    else:
        retVal = right
        retVal.n = mergeSort(left, right.n)
    return retVal

# Return -3 -> 1 -> 4 -> 99 -> None
in1 = Node(4, Node(1, Node(-3, Node(99))))
printLL(in1)
in2 = Solution(in1)
printLL(in2)

#
print()
# 

# Return 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
in1 = Node(0, Node(1, Node(3, Node(2, Node(5, Node(6, Node(4, Node(7, Node(10, Node(8, Node(9)))))))))))
printLL(in1)
in2 = Solution(in1)
printLL(in2)