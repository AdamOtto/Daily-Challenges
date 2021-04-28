"""
Given a collection of intervals, find the minimum number of intervals you need
to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2],
but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1
as the last interval can be removed and the first two won't overlap.
"""

def CheckOverlap(p1, p2):
    if p1[0] > p2[0] and p1[0] < p2[1]:
        return True
    elif p1[1] > p2[0] and p1[1] < p2[1]:
        return True

    if p2[0] > p1[0] and p2[0] < p1[1]:
        return True
    elif p2[1] > p1[0] and p2[1] < p1[1]:
        return True

    return False

# O(nlog(n))
def Solution(n):
    n.sort(key = lambda a:a[0])
    #print(n)
    l = len(n)
    retVal = []
    for i in range(1, l):
        if not CheckOverlap(n[i - 1], n[i]):
            retVal.append(n[i - 1])

    if not CheckOverlap(retVal[len(retVal) - 1], n[l - 1]):
        retVal.append(n[l - 1])
    #print(retVal)
    return l - len(retVal)




#in1 = [(7, 9), (2, 4), (5, 8)]
in1 = [ (1,2), (2,3), (3,4), (4,10), (4,5), (5,6) ]
print(Solution(in1))