"""
Given an undirected graph represented as an adjacency matrix and an integer k,
write a function to determine whether each vertex in the graph can be colored such that
no two adjacent vertices share the same color using at most k colors.
"""
def Solution(ar, k):
    colours = {}
    ResetColours(colours)
    firstNode = None
    
    for key, val in ar.items():
            if firstNode is None:
                firstNode = key
            colours[key] = None
    
    if Helper(firstNode, ar, colours, k):
        return True
    
    return False

def ResetColours(colours):
    for key, val in colours.items():
        val = None
    
def Helper(cur, ar, colours, k):
    if colours[cur] is not None:
        return False
    for i in range(0, k):
        colours[cur] = i
        res = CheckGraph(ar, colours)
        if res == 2:
            for nei in ar[cur]:
                if Helper(nei, ar, colours, k):
                    return True
        elif res == 1:
            return True
    colours[cur] = None
    return False
    

# 2 means graph isn't fully coloured in.
# 1 means graph is valid
# 0 means graph is invalid
def CheckGraph(ar, colours):
    # Check for uncoloured graphs
    for key, val in colours.items():
        if val is None:
            return 2
    # Check adjacent colours
    for key, val in ar.items():
        for v in val:
            if colours[v] == colours[key]:
                return 0
    return 1

# Return True
in1 = { 1 : [2, 3],
        2 : [1, 3],
        3 : [1, 2]}
print(Solution(in1, 3))
# Return False
print(Solution(in1, 2))

# Return True
in1 = { 1 : [2, 3],
        2 : [1, 3],
        3 : [1, 2, 4, 5],
        4 : [3, 5],
        5:  [3, 4]}
print(Solution(in1, 3))
# Return False
print(Solution(in1, 2))