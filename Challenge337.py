"""
Given a linked list, uniformly shuffle the nodes. What if we want to prioritize space over time?
"""
import random

class LinkedList:
    val = None
    n = None
    def __init__(self, Value, Next=None):
        self.val = Value
        self.n = Next

def printLL(head):
    temp = head
    prVal = ""
    while temp != None:
        prVal += str(temp.val) + " -> "
        temp = temp.n
    print(prVal)        

def Solution(head, N):
    
    for i in range(N):
        #printLL(head)
        swap1 = swap2 = 0
        while swap1 == swap2:
            swap1 = random.randint(0, N - 1)
            swap2 = random.randint(0, N - 1)
        prev1, cur1 = getElement(head, swap1)
        prev2, cur2 = getElement(head, swap2)
        
        if swap1 == 0:
            head = swapHead(head, prev1, cur1, prev2, cur2)
        elif swap2 == 0:
            head = swapHead(head, prev2, cur2, prev1, cur1)
        else:
            swap(prev1, cur1, prev2, cur2)
    return head

def getElement(head, swap):
    cur = head
    prev = head
    for i in range(swap):
        cur = cur.n
        if prev.n != cur:
            prev = prev.n
    return prev, cur

def swap(prev1, cur1, prev2, cur2):
    prev1.n = cur2
    prev2.n = cur1
    temp = cur1.n
    cur1.n = cur2.n
    cur2.n = temp
    return

def swapHead(head, prev1, cur1, prev2, cur2):
    prev2.n = cur1
    temp = cur1.n
    cur1.n = cur2.n
    cur2.n = temp
    head = cur2
    return head

N = 5
in1 = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
printLL(in1)
in1 = Solution(in1, N)
printLL(in1)