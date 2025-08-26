"""
In a directed graph, each node is assigned an uppercase letter.
We define a path's value as the number of most frequently-occurring letter along that path.
For example, if a path in the graph goes through "ABACA", the value of the path is 3,
since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges,
return the largest value path of the graph.
If the largest value is infinite, then return null.

The graph is represented with a string and an edge list.
The i-th character represents the uppercase letter of the i-th node.
Each tuple in the edge list (i, j) means there is a directed edge from the i-th node
to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A
[(0, 0)]
Should return null, since we have an infinite loop.
"""
def Solution(Letters, Paths):
    l = len(Letters)
    visited = [False] * l
    d = {}
    p = {}
    for i in range(l):
        if Letters[i] not in d:
            d[Letters[i]] = 0
        p[i] = []
    for i in range(len(Paths)):
        p[Paths[i][0]].append(Paths[i][1])
    retVal = 0
    for i in range(l):
        temp = d.copy()
        if not visited[i]:
            if Helper(i, visited, Letters, p, temp):
                for key, val in temp.items():
                    retVal = max(retVal, val)
            else:
                return None
    
    return retVal

def Helper(i, visited, Letters, p, temp, start = None):
    if start is not None:
        if i == start:
            return False
    else:
        start = i
    if visited[i]:
        return True
    visited[i] = True
    temp[Letters[i]] += 1
    for nextNode in p[i]:
        if not Helper(nextNode, visited, Letters, p, temp, start):
            return False
    return True

# Return 3
print(Solution("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]))    

# Return None
print(Solution("A", [(0, 0)]))

# Return None
print(Solution("ABCDEFA", [(0, 5), (1, 2), (2, 3), (3, 4), (5,6), (6, 0)]))    

# Return 2
print(Solution("ABCDEFA", [(0, 5), (1, 2), (2, 3), (3, 4), (5,6)]))

# Return 3
print(Solution("ABACDEA", [(0, 1), (0, 2), (1, 3), (2, 3), (3,4), (4,5), (5,6)])) 