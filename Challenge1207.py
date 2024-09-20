"""
Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""
class ll:
    val = n = None
    
    def __init__(self, value, NextNode = None):
        self.val = value
        self.n = NextNode
        
def printLL(ar):
    temp = ar
    st = ""
    while temp != None:
        st += str(temp.val) + " -> "
        temp = temp.n
    st += "None"
    print(st)

def Solution(ar, k):
    start = mid = last = ar
    midCount = 0
    lastCount = 0
    
    while last.n is not None:
        mid = mid.n
        midCount += 1
        last = last.n
        lastCount += 1
        if last.n is not None:
            last = last.n
            lastCount += 1
    
    if k > lastCount:
        return
    if k == lastCount:
        ar = ar.n
        return ar
    
    if lastCount - k == midCount:
        while start.n != mid:
            start = start.n
        start.n = mid.n
    if lastCount - k > midCount:
        temp = mid
        mid = mid.n
        midCount += 1
        while midCount < lastCount - k:
            mid = mid.n
            temp = temp.n
            midCount += 1
        temp.n = mid.n
    if lastCount - k < midCount:
        temp = start
        start = start.n
        startCount = 1
        while startCount < lastCount - k:
            start = start.n
            temp = temp.n
            startCount += 1
        temp.n = start.n
    return ar

# init linked list
in1 = ll(1)
temp = in1
for i in range(2, 100):
    temp.n = ll(i)
    temp = temp.n
printLL(in1)

# Remove 99
in1 = Solution(in1, 0)
printLL(in1)

# Remove 86
in1 = Solution(in1, 12)
printLL(in1)