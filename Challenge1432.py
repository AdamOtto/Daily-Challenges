"""
Given the head to a singly linked list, where each node also has a “random”
pointer that points to anywhere in the linked list, deep clone the list.

Assume: Each value in the linked list is unique.
"""
class LL:
    val = None
    n = None
    r = None
    def __init__(self, Value, Next = None, Random = None):
        self.val = Value
        self.n = Next
        self.r = Random

def printLL(ll):
    temp = ll
    retVal = ""
    while temp is not None:
        retVal += str(temp.val) + " -> "
        temp = temp.n
    print(retVal + "None")

def getLLind(ll, ind):
    i = 0
    temp = ll
    while i < ind and temp is not None:
        temp = temp.n
        i += 1
    if i == ind:
        return temp
    return None

def Solution(ar):
    newHead = LL(ar.val)
    temp = ar.n
    nHtrav = newHead
    indTracker = [ar.val]
    while temp is not None:
        indTracker.append(temp.val)
        nHtrav.n = LL(temp.val)
        nHtrav = nHtrav.n
        temp = temp.n
    
    temp = ar
    nHtrav = newHead
    while temp is not None:
        ind1 = indTracker.index(temp.val)
        ind2 = indTracker.index(temp.r.val)
        getLLind(nHtrav, ind1).r = getLLind(nHtrav, ind2)
        temp = temp.n
    return newHead

def CompareLL(ar1, ar2):
    t1 = ar1
    t2 = ar2
    while t1 is not None and t2 is not None:
        if t1.val == t2.val and t1.r.val == t2.r.val:
            t1 = t1.n
            t2 = t2.n
        else:
            return False
    return True

# Return clones list.  CompareLL should return True
in1 = LL(1, LL(2, LL(3, LL(4))))
printLL(in1)
getLLind(in1, 0).r = getLLind(in1, 3)
getLLind(in1, 1).r = getLLind(in1, 2)
getLLind(in1, 2).r = getLLind(in1, 0)
getLLind(in1, 3).r = in1
in2 = Solution(in1)
printLL(in2)
print(CompareLL(in1, in2))