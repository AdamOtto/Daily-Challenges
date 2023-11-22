"""
Given an undirected graph G, check whether it is bipartite.
Recall that a graph is bipartite if its vertices can
be divided into two independent sets, U and V,
such that no edge connects vertices of the same set.
"""

def Solution(ar):

    for key, val in ar.items():
        colorGraph = {}
        colorGraph[key] = True
        graphFound = True
        nextNode = []
        for a in val:
            nextNode.append( (key, a) )
        
        while len(nextNode) > 0:
            lastNode, cur = nextNode.pop(0)
            
            if cur in colorGraph:
                # Can't separate graphs.
                if colorGraph[cur] == colorGraph[lastNode]:
                    graphFound = False
                    break
            else:
                colorGraph[cur] = not colorGraph[lastNode]
                for a in ar[cur]:
                    nextNode.append( (cur, a) )
        if graphFound and len(colorGraph) == len(ar):
            return True
    return False
   
# Return True
graph = { 0: [1,5],
          1: [0, 2],
          2: [1, 3],
          3: [2, 4],
          4: [3, 5],
          5: [4, 0]
}
print(Solution(graph))

# Return False
graph = { 0: [1,4],
          1: [0, 2],
          2: [1, 3],
          3: [2, 4],
          4: [3, 0],
          5: []
}
print(Solution(graph))

# Return False
graph = { 0: [1, 2],
          1: [0, 2],
          2: [1, 3],
          3: [0, 2]
}
print(Solution(graph))

# Return True
graph = { 0: [1, 2],
          1: [0, 3],
          2: [0, 3],
          3: [1, 2, 4, 5],
          4: [3, 6],
          5: [3, 6],
          6: [4, 5]
}
print(Solution(graph))