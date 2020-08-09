"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
"""


class linkedList:
    value = 0
    nextn = None


def makeLinkedListFromArray(inp):
    retVal = linkedList()
    retVal.value = inp[0]
    t = retVal
    for i in range(1, len(inp)):
        temp = linkedList()
        temp.value = inp[i]
        t.nextn = temp
        t = t.nextn
    return retVal


def FindLinkeListIntersect(ll1, ll2):
    t1 = ll1
    t2 = ll2
    d1 = {}
    d2 = {}
    while t1.nextn is not None or t2.nextn is not None:
        d1[t1.value] = t1.value
        d2[t2.value] = t2.value
        if t1.value in d2:
            return t1.value
        elif t2.value in d1:
            return t2.value
        t1 = t1.nextn
        t2 = t2.nextn

    # Check if last elements match
    d1[t1.value] = t1.value
    d2[t2.value] = t2.value
    if t1.value in d2:
        return t1.value
    elif t2.value in d1:
        return t2.value
    else:
        return "No intersect"


in1 = [1, 2, 3, 4, 5, 6]
in2 = [11, 12, 4, 13, 14, 15]
ll1 = makeLinkedListFromArray(in1)
ll2 = makeLinkedListFromArray(in2)
print(FindLinkeListIntersect(ll1, ll2))