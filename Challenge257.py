"""
Given an array of integers out of order, determine the bounds of
the smallest window that must be sorted in order for the entire array to be sorted.

For example, given [3, 7, 5, 6, 9], you should return (1, 3).
"""

def Solution1(ar):
    ar2 = sorted(ar)
    #print(ar2)
    l = len(ar)
    lowBounds = None
    highBounds = None
    for i in range(l):
        if ar[i] != ar2[i]:
            if lowBounds is None:
                lowBounds = i
            highBounds = i
    return (lowBounds, highBounds)

def Solution2(ar):
    l = len(ar)

    lowBounds = None
    highBounds = l - 1
    for i in range(l - 1):
        if ar[i] > ar[i + 1]:
            lowBounds = i
            break
    if lowBounds is None:
        return (None, None)

    for i in reversed(range(0, l)):
        if ar[i - 1] > ar[i]:
            highBounds = i
            break


    minVal = ar[lowBounds]
    maxVal = ar[lowBounds]
    for i in range(lowBounds, highBounds + 1):
        if ar[i] > maxVal:
            maxVal = ar[i]
        if ar[i] < minVal:
            minVal = ar[i]

    for i in range(lowBounds):
        if ar[i] > minVal:
            lowBounds = i
            break
    for i in reversed((range(highBounds, l))):
        if ar[i] < maxVal:
            highBounds = i
            break

    return (lowBounds, highBounds)



in1 = [3, 7, 5, 6, 9]
print(Solution1(in1))
print(Solution2(in1))
print()

in1 = [0,1,2,3,4,6,5]
print(Solution1(in1))
print(Solution2(in1))
print()

in1 = [1,2,0,3,4,5,6]
print(Solution1(in1))
print(Solution2(in1))
print()

in1 = [1,2,3,4,5]
print(Solution1(in1))
print(Solution2(in1))
print()