"""
Given a linked list, rearrange the node values such that they appear
in alternating low -> high -> low -> high ... form.

For example, given 1 -> 2 -> 3 -> 4 -> 5,
you should return 1 -> 3 -> 2 -> 5 -> 4 or 1 -> 4 -> 2 -> 5 -> 3, 1 -> 5 -> 2 -> 4 -> 3, etc.
"""

class LL:
    val = None
    n = None
    
    def __init__(self, value, next = None):
        self.val = value
        self.n = next

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

def sortLL(ar):
    if ar is None or ar.n is None:
        return ar
    middle = getMiddle(ar)
    nextMiddle = middle.n
    middle.n = None
    left = sortLL(ar)
    right = sortLL(nextMiddle)
    
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

def Solution(ar):
    smallerHalf = sortLL(ar)
    middle = getMiddle(smallerHalf)
    largerHalf = middle.n
    middle.n = None
    retVal  = cur = smallerHalf
    smallerHalf = smallerHalf.n
    while largerHalf != None or smallerHalf != None:
        if largerHalf != None:
            cur.n = largerHalf
            cur = cur.n
            largerHalf = largerHalf.n
        if smallerHalf != None:
            cur.n = smallerHalf
            cur = cur.n
            smallerHalf = smallerHalf.n
    return retVal

# Return 1 -> 4 -> 2 -> 5 -> 3 -> None
in1 = LL(1, LL(2, LL(3, LL(4, LL(5)))))
Solution(in1)
printLL(in1)

# Return 1 -> 4 -> 2 -> 5 -> 3 -> None
in1 = LL(5, LL(3, LL(4, LL(1, LL(2)))))
in1 = Solution(in1)
printLL(in1)

# Return 1 -> 101 -> 13 -> 139 -> 63 -> 141 -> 81 -> 492 -> 100 -> None
in1 = LL(100, LL(101, LL(63, LL(13, LL(81, LL(139, LL(141, LL(1, LL(492)))))))))
in1 = Solution(in1)
printLL(in1)