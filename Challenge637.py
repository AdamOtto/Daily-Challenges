"""
Given a list of possibly overlapping intervals, return a new list
of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)],
you should return [(1, 3), (4, 10), (20, 25)].
"""

def Solution(ar):
    l = len(ar)
    ar = sorted(ar, key=lambda tup: tup[0])
    start = ar[0][0]
    end = ar[0][1]
    retVal = []
    for i in range(1, l):
        if ar[i][0] > end:
            retVal.append( (start, end) )
            start = ar[i][0]
            end = ar[i][1]
        else:
            end = max(end, ar[i][1])
    retVal.append( (start, end) )
    return retVal

# Return [(1, 3), (4, 10), (20, 25)]
print(Solution([(1, 3), (5, 8), (4, 10), (20, 25)]))

# Return [(1, 11)]
print(Solution([(1, 5), (2, 6), (7, 10), (2, 11)]))

# Return [(1, 3), (4, 6), (7, 12)]
print(Solution([(1, 3), (4, 6), (7, 10), (9, 12)]))