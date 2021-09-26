"""
At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity").
To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.
"""

class knows:
    rel = None
    def __init__(self, relations):
        self.rel = relations
    
    def AknowsB(self, a, b):
        if b in self.rel[a]:
            return True
        return False

# O(N)
def Solution(N, knows):
    temp = []
    temp.extend(N)
    A = temp.pop()
    B = temp.pop()
    while len(temp) > 1:
        if knows.AknowsB(A, B):
            A = temp.pop()
        else:
            B = temp.pop()
    
    if len(temp) == 0:
        return False
    
    C = temp.pop()
    
    if knows.AknowsB(C, B):
        C = B
    if knows.AknowsB(C, A):
        C = A
    
    for i in range(len(N)):
        if N[i] != C and ( knows.AknowsB(C, N[i]) or not knows.AknowsB(N[i], C)):
            return False
    return C
    

# Celebrity is 0
rel = { 0: {},
        1: {0,2},
        2: {0,1,4},
        3: {0,4},
        4: {0,2,3}
}
in1 = [0,1,2,3,4]
in2 = knows(rel)
print(Solution(in1, in2))


# Celebrity is C
rel = { 'A': {'B', 'C'},
        'B': {'A', 'C', 'D'},
        'C': {},
        'D': {'B', 'C', 'F'},
        'E': {'G', 'C'},
        'F': {'B', 'C'},
        'G': {'C', 'E'}
}
in1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
in2 = knows(rel)
print(Solution(in1, in2))

# Return False
rel = { 'A': {'B', 'C'},
        'B': {'A', 'C', 'D'},
        'C': {'B'},
        'D': {'B', 'C', 'F'},
        'E': {'G', 'C'},
        'F': {'B', 'C'},
        'G': {'E', 'C'}
}
in1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
in2 = knows(rel)
print(Solution(in1, in2))