"""
A graph is minimally-connected if it is connected and there
is no edge that can be removed while still leaving the graph connected.
For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected.
You can choose to represent the graph as either an adjacency matrix or adjacency list.
"""

def Solution(ar):
    edges = []
    visited = set()
    for key, val in ar.items():
        if len(val) > 0:
            visited.add(key)
            for i in range(len(val)):
                if val[i] not in visited:
                    edges.append( (key, val[i]) )
    
    if len(ar) - 1 == len(edges):
        return True
    return False

# Return True
in1 = { 0:[2,5],
        1:[],
        2:[0,1,3],
        3:[],
        4:[],
        5:[0,4,6],
        6:[]
}
print(Solution(in1))

# Return False
in1 = { 0:[5,1],
        1:[0,2],
        2:[1,3],
        3:[2,4],
        4:[3,5],
        5:[4,0]
}
print(Solution(in1))