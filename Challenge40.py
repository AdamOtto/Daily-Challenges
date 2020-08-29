"""
Given an array of integers where every integer occurs three times except for one integer,
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
"""

def Solution(in1):
    itemsCount = int(((len(in1) - 1) / 3) + 1)
    val = [None] * itemsCount
    count = [0] * itemsCount
    for i in in1:
        if i not in val:
            AddItem(val, i, itemsCount)
        t = val.index(i)
        count[t] += 1

    t = count.index(1)
    print(val[t])

def AddItem(li, it, itemsCount):
    for i in range(0, itemsCount):
        if li[i] is None:
            li[i] = it
            return
    return

#in1 = [6, 1, 3, 3, 3, 6, 6]
#in1 = [13, 19, 13, 13]
in1 = [1,2,7,3,4,1,2,5,-1,7,3,0,4,1,2,3,-1,4,5,7,5,6,-1,6,6]
Solution(in1)
