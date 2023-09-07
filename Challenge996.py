"""
Recall that the minimum spanning tree is the subset of edges of a tree that
connect all its vertices with the smallest possible total edge weight.
Given an undirected graph with weighted edges,
compute the maximum weight spanning tree.
"""
import sys
def maximumSpanningTree(graph):
    l = len(graph)
    visited = [False] * l
    weights = [-sys.maxsize] * l;
    parent = [0] * l

    weights[0] = sys.maxsize
    parent[0] = -1

    for i in range(l - 1):
        MaxVertIndex = findMaxVertex(visited, weights, l)
        visited[MaxVertIndex] = True
        for j in range(l):
            if graph[j][MaxVertIndex] > weights[j] and visited[j] is False:
                weights[j] = graph[j][MaxVertIndex];
                parent[j] = MaxVertIndex;
    return sum(weights[1:])

def findMaxVertex(visited, weights, l):
    retVal = -1;
    maxW = -sys.maxsize;
    for i in range(l):
        if visited[i] == False and weights[i] > maxW:
            maxW = weights[i];
            retVal = i;
    return retVal;

# Return 6
graph = [[1,2,3], [3,2,3], [3,2,1]]
print(maximumSpanningTree(graph))

# Return 30
graph = [[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]]
print(maximumSpanningTree(graph))