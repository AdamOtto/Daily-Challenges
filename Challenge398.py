"""
Given a linked list and an integer k, remove the k-th node from
the end of the list and return the head of the list.

k is guaranteed to be smaller than the length of the list.

Do this in one pass.

Note:
Assume k = 0 means remove the last element.
"""

class linkedList:
    v = None
    n = None
    
    def __init__(self, value, next = None):
        self.v = value
        self.n = next
    
def Solution(ar, k):
    prev = ar
    cur = ar.n
    last = cur.n
    #print("prev:",prev.v)
    #print("cur:",cur.v)
    for i in range(k - 1):
        last = last.n
    #print("last:",last.v)
    #print("----------")
    while last.n is not None:
        last = last.n
        cur = cur.n
        prev = prev.n
    #print("prev:",prev.v)
    #print("cur:",cur.v)
    #print("last:",last.v)
    if k == 0:
        cur.n = None
    else:
        prev.n = cur.n
        cur = None
    return
    
def printLL(ar):
    prStr = ""
    t = ar
    while t.n is not None:
        prStr += str(t.v) + " -> "
        t = t.n
    prStr += str(t.v)
    print(prStr)

# Remove 3
print("Remove 3 from this linked list:")
in1 = linkedList(1, linkedList(2, linkedList(3, linkedList(4, linkedList(5)))))
k = 2
printLL(in1)
Solution(in1, k)
printLL(in1)

print("-----------")

# Remove 5
print("Remove 5 from this linked list:")
in1 = linkedList(1, linkedList(2, linkedList(3, linkedList(4, linkedList(5)))))
k = 0
printLL(in1)
Solution(in1, k)
printLL(in1)


print("-----------")

# Remove 4
print("Remove 4 from this linked list:")
in1 = linkedList(1, linkedList(2, linkedList(3, linkedList(4, linkedList(5)))))
k = 1
printLL(in1)
Solution(in1, k)
printLL(in1)