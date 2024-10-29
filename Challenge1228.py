"""
Given a list of possibly overlapping intervals, return a new list of intervals
where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)],
you should return [(1, 3), (4, 10), (20, 25)].
"""
def Solution(ar):
    t = sorted(ar, key=lambda x: x[0])
    i = 1
    while i < len(t):
        if t[i - 1][1] > t[i][0]:
            temp1 = t.pop(i - 1)
            temp2 = t.pop(i - 1)
            i = max(1, i - 1)
            t.insert(i, (min(temp1[0], temp2[0]), max(temp1[1], temp2[1])) )
        else:
            i += 1
    return t
    

# Return [(1, 3), (4, 10), (20, 25)]
print(Solution([(1, 3), (5, 8), (4, 10), (20, 25)]))

# Return [(1, 7)]
print(Solution([(1, 4), (3, 5), (2, 6), (5, 7)]))