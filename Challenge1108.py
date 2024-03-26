"""
Given an undirected graph,
determine if it contains a cycle.
"""

def Solution(ar):
    for key, value in ar.items():
        for v in value:
            visited = set()
            if Helper(key, v, ar, visited):
                return True
    return False
        
def Helper(first, cur, ar, visited):
    if cur == first:
        return True
    visited.add(cur)
    if cur in ar:
        for n in ar[cur]:
            if n not in visited:
                if Helper(first, n, ar, visited):
                    return True
    return False

# Return True
in1 = { 0:[1,2],
        1:[2],
        2:[3],
        3:[1,5],
        4:[0],
        5:[4]
}
print(Solution(in1))

# Return False
in1 = { 0:[2],
        2:[],
}
print(Solution(in1))

# Return True
in1 = { 0:[1,2],
        1:[],
        2:[3],
        3:[0]
}
print(Solution(in1))