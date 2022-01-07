"""
The transitive closure of a graph is a measure of which
vertices are reachable from other vertices.
It can be represented as a matrix M, where M[i][j] == 1 if there is a path
between vertices i and j, and otherwise 0.

For example, suppose we are given the
following graph in adjacency list form:

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
The transitive closure of this graph would be:

[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Given a graph, find its transitive closure.
"""


def Solution(ar):
    l = len(ar)
    tranClose = [[0 for i in range(l)] for j in range(l)]
    
    for i in range(0, l):
        Helper(i, ar, tranClose, i)
    return tranClose

def Helper(cur, ar, tranClose, initNode):
    
    for i in range(len(ar[cur])):
        temp1 = ar[cur][i]
        temp2 = tranClose[initNode][ar[cur][i]]
        if tranClose[initNode][ar[cur][i]] == 0:
            tranClose[initNode][ar[cur][i]] = 1
            if initNode != ar[cur][i]:
                Helper(ar[cur][i], ar, tranClose, initNode)
    return

# Should return [[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
in1 = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
print(Solution(in1))

# Should return [[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1]]
in1 = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3]
]
print(Solution(in1))