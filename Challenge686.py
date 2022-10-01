"""
You are given a tree with an even number of nodes.
Consider each connection between a parent and child node to be an "edge".
You would like to remove some of these edges, such that the disconnected subtrees
that remain each have an even number of nodes.
For example, suppose your input was the following tree:
   1
  / \ 
 2   3
    / \ 
   4   5
 / | \
6  7  8
In this case, removing the edge (3, 4) satisfies our requirement.
Write a function that returns the maximum number of edges you can
remove while still satisfying this requirement.
"""

def Solution(edges, top, N):
    visited = {}
    for key, val in edges.items():
        visited[key] = False
    helper(edges, top, visited, N)
    return retVal

def helper(edges, cur, visited, N):
    global retVal
    visited[cur] = True
    curNodeCount = 0
    
    for v in edges[cur]:
        subTreeCount = 0
        if not visited[v]:
            subTreeCount = helper(edges, v, visited, N)
        if subTreeCount % 2 == 0:
            retVal += 1
        else:
            curNodeCount += subTreeCount
    return curNodeCount + 1

edges = { 1: [2,3],
          2: [],
          3: [4,5],
          4: [6,7,8],
          5: [],
          6: [],
          7: [],
          8: []
}
top = 1
N = 8
retVal = 0
Solution(edges, top, N)
print(retVal)