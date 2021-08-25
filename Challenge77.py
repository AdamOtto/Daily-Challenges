"""
Given a list of possibly overlapping intervals, return a new list
of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)],
you should return [(1, 3), (4, 10), (20, 25)].
"""

# O(nlog(n))
def Solution(ar):
    l = len(ar)
    ar = sorted(ar, key=lambda x:x[0])
    i = 1
    while i < len(ar):
        if ar[i - 1][1] >= ar[i][0]:
            t1 = ar.pop(i - 1)
            t2 = ar.pop(i - 1)
            ar.insert(i - 1, (t1[0], max(t1[1], t2[1])))
        else:
            i += 1
    return ar

in1 = [(1, 3), (4, 10), (5, 8), (20, 25)]
print(Solution(in1))

in1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(Solution(in1))

in1 = [(1, 8), (3, 4), (5, 6), (7, 8)]
print(Solution(in1))

in1 = [(15, 19), (94, 102), (40, 53), (18, 24), (38, 58), (20, 79), (89, 94)]
print(Solution(in1))