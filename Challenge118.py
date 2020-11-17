'''
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
'''
import math
#import random

# O(nlog(n))
def Solution(in1):
    retVal = []
    for i in in1:
        InsertInto(i * i, retVal)
    return retVal


def InsertInto(x, sqr):
    l = len(sqr)
    if l == 0:
        sqr.append(x)
        return
    elif l == 1:
        if x >= sqr[0]:
            sqr.append(x)
        else:
            sqr.insert(0, x)
        return
    i = int(l / 2)
    lastI = 0
    while i > 0 and i < l:
        if sqr[i - 1] <= x and x <= sqr[i]:
            sqr.insert(i, x)
            return
        if sqr[i - 1] > x:
            t = i
            i = int(math.floor((i + lastI) / 2))
            lastI = t
            if lastI == i:
                i -= 1
        elif x > sqr[i]:
            lastI = i
            i = int(math.ceil((lastI + l) / 2))

    if i == 0:
        sqr.insert(0, x)
    elif i == l:
        sqr.insert(l, x)


#in1 = [-9, -2, 0, 2, 3]
in1 = [2,6,1,2,4,7,19,2,1,0,3,9,0,4,3,5,8,12,22,11,1,100,9,10,15,14,1,3,4,6,5,2,17,75,25]

t = Solution(in1)
print(t)