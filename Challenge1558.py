"""
A classroom consists of N students, whose friendships can be represented in an adjacency list.
For example, the following descibes a situation where 0 is friends
with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 
Each student can be placed in a friend group, which can be defined as the
transitive closure of that student's friendship relations.
In other words, this is the smallest set such that no student
in the group has any friends outside this group.

For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above,
determine the number of friend groups in the class.
"""
def Solution(ar):
    cliques = []
    visited = set()
    for key, value in ar.items():
        if key not in visited:
            group = []
            getClique(key, ar, group)
            group = sorted(group)
            for g in group:
                visited.add(g)
            #if group not in cliques:
            cliques.append(group)
    return len(cliques), cliques

def getClique(cur, ar, visited):
    if cur not in visited:
        visited.append(cur)
    else:
        return
    
    for friends in ar[cur]:
        getClique(friends, ar, visited)
    return

# Return 3, [[0, 1, 2, 5], [3, 6], [4]]
in1 = { 0: [1, 2],
        1: [0, 5],
        2: [0],
        3: [6],
        4: [],
        5: [1],
        6: [3]} 
print(Solution(in1))

# Return 2, [['A', 'B', 'C', 'D', 'F'], ['E']]
in1 = { 'A': ['D', 'F'],
        'B': ['C', 'D'],
        'C': ['B'],
        'D': ['A', 'B','F'],
        'E': [],
        'F': ['A', 'D'] }
print(Solution(in1))