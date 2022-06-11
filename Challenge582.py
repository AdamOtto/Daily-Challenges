"""
Let X be a set of n intervals on the real line.
We say that a set of points P "stabs" X if every interval in X contains
at least one point in P. Compute the smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)],
you should return [4, 9].
"""

def Solution(ar):
    l = len(ar)
    temp = sorted(ar, key=lambda x: x[1])
    retVal = set()
    visited = set()
    
    for i in range(l):
        for j in range(i + 1, l):
            if temp[i][1] >= temp[j][0] and j not in visited:
                retVal.add(temp[i][1])
                visited.add(i)
                visited.add(j)
            else:
                break
    if len(visited) != l:
        for i in range(l):
            if i not in visited:
                retVal.add(temp[i][1])
    
    return list(sorted(list(retVal)))


# Return [4, 9]
print(Solution([(1, 4), (4, 5), (7, 9), (9, 12)]))

# Return [3, 5, 10, 12]
print(Solution([(1,3), (4,5), (6,10), (11,12)]))

# Return [6, 12]
print(Solution([(1,6), (4,6), (6,10), (11,12)]))

# Return [6]
print(Solution([(1,11), (4,6), (6,7), (6,12)]))