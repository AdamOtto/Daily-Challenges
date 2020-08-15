"""
Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.
"""

class linkedList:
    value = 0
    nextn = None

"""
# Misunderstood problem, though 'remove kth element from list'
def Solution(inp, k):

    if k == 0:
        return inp.nextn
    lastLL = inp
    cur = inp.nextn

    for i in range(1,k):
        lastLL = cur
        cur = cur.nextn
    #printLinkedList(cur)
    #printLinkedList(lastLL)
    lastLL.nextn = cur.nextn
    return inp
"""

# Solution 2, runs in O(n + k) time.  Closer k is to beginning, the longer it takes.
def Solution(inp, k):
    lastLL = inp
    cur = inp.nextn
    t = SolHelper(lastLL, cur, k)
    if t == k:
        return inp.nextn
    return inp

def SolHelper(lastLL, cur, k):

    if cur is None:
        return 0
    t = SolHelper(lastLL.nextn, cur.nextn, k)
    if t == k:
        lastLL.nextn = cur.nextn
    return t + 1

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

def printLinkedList(inp):
    strVal = ""
    cur = inp
    while cur.nextn is not None:
        strVal += str(cur.value) + "->"
        cur = cur.nextn
    strVal += str(cur.value)
    print(strVal)


inp = [1,2,3,4,5]
ll = makeLinkedListFromArray(inp)
printLinkedList(ll)
k = 4
print("Remove " + str(k) + " index from linked list:")
ll = Solution(ll, k)
printLinkedList(ll)