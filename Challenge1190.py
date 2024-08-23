"""
A network consists of nodes labeled 0 to N.
You are given a list of edges (a, b, t),
describing the time t it takes for a message to be sent from node a to node b.
Whenever a node receives a message, it immediately passes the message
on to a neighboring node, if possible.

Assuming all nodes are connected, determine how long it will
take for every node to receive a message that begins at node 0.

For example, given N = 5, and the following edges:

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take that much time.
"""

def Solution(N, edges):
    l = len(edges)
    d = {}
    Helper(0, 0, l, edges, d)
    retVal = 0
    for key, value in d.items():
        retVal = max(retVal, value)
    return retVal
    
def Helper(cur, travel, N, edges, d):
    if cur not in d:
        d[cur] = travel
    elif d[cur] > travel:
        d[cur] = travel
    
    temp = []
    for i in range(N):
        if edges[i][0] == cur:
            temp.append(edges[i])
    
    temp = sorted(temp, key=lambda x: x[2])
    
    for i in range(len(temp)):
        if temp[i][1] not in d:
            Helper(temp[i][1], travel + temp[i][2], N, edges, d)
        elif temp[i][1] in d and travel + temp[i][2] < d[temp[i][1]]:
            Helper(temp[i][1], travel + temp[i][2], N, edges, d)
    return
        
    
# Return 9
N = 5
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
print(Solution(N, edges))