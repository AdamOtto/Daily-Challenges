"""
The transitive closure of a graph is a measure of which
vertices are reachable from other vertices.
It can be represented as a matrix M, where M[i][j] == 1
if there is a path between vertices i and j, and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

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

def Solution(graph):
    l = len(graph)
    retVal = [[0 for i in range(l)] for j in range(l)]

    for i in range(l):
        s = set()
        Helper(i, graph, s)
        for elem in s:
            retVal[i][elem] = 1

    for i in range(l):
        s = ""
        for j in range(l):
            s += str(retVal[i][j]) + " "
        print(s)

def Helper(curNode, graph, visited):
    if curNode not in visited:
        visited.add(curNode)

    for nodes in graph[curNode]:
        if nodes not in visited:
            Helper(nodes, graph, visited)
    return

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
Solution(graph)
print("\n")

graph = [
    [3],
    [0],
    [2],
    [4],
    [5],
    [0]
]
Solution(graph)