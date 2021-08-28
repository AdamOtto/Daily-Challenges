"""
Given a linked list, remove all consecutive nodes that sum to zero.
Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6.
In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
"""


class llist:
    val = None
    n = None
    
    def __init__(self, value, next = None):
        self.val = value
        self.n = next

def Solution(top):
    start = top
    end = top.n
    
    while end != None:
        start = top
        while start != end:
            if llSum(start, end) == 0:
                if top == start:
                    top = end.n
                    start = end.n
                    for i in range(2):
                        if end is not None:
                            end = end.n
                else:
                    t = top
                    while t.n != start:
                        t = t.n
                    t.n = end.n
                    start = end.n
                    for i in range(2):
                        if end is not None:
                            end = end.n
                break
            start = start.n
        if end is not None:
            end = end.n
    return top

def llSum(start, end):
    count = 0
    t = start
    while t != end:
        count += t.val
        t = t.n
    return count + end.val

def printLL(ar):
    if ar is None:
        print("empty")
    t = ar
    retVal = ""
    while t is not None:
        retVal += str(t.val) + " > "
        t = t.n
    print(retVal)

# Return 5
in1 = llist(3, llist(4, llist(-7, llist(5, llist(6, llist(-6))))))
printLL(in1)
print("Becomes...")
start = in1
end = in1.n.n
in1 = Solution(in1)
printLL(in1)

print()

# Return 1 > 2 > 3 > 4
in1 = llist(1, llist(2, llist(3, llist(4))))
printLL(in1)
print("Becomes...")
start = in1
end = in1.n.n
in1 = Solution(in1)
printLL(in1)

print()

# Return empty
in1 = llist(1, llist(2, llist(3, llist(4, llist(-10)))))
printLL(in1)
print("Becomes...")
start = in1
end = in1.n.n
in1 = Solution(in1)
printLL(in1)

print()

# Return 2 > 8 > 6
in1 = llist(2, llist(15, llist(-15, llist(8, llist(3, llist(-5, llist(4, llist(-2, llist(6)))))))))
printLL(in1)
print("Becomes...")
start = in1
end = in1.n.n
in1 = Solution(in1)
printLL(in1)