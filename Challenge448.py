"""
Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first,
the Gs come second, and the Bs come last.
You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

def Solution(in1):
    Ri = 0
    Gi = 0
    Bi = 0
    i  = 0
    
    while i < len(in1):
        if in1[i] == 'R':
            if i > Ri:
                swap(in1, i, Ri)
                Ri += 1
                if Ri >= Gi:
                    Gi += 1
                    if Gi >= Bi:
                        Bi += 1
            else:
                i += 1
            continue
        if in1[i] == 'G':
            if i > Gi:
                swap(in1, i, Gi)
                Gi += 1
                if Gi >= Bi:
                        Bi += 1
            else:
                i += 1
            continue
        if in1[i] == 'B':
            if i > Bi:
                swap(in1, i, Bi)
                Bi += 1
            else:
                i += 1
            continue
        
    return in1
        
        
def swap(l, pos1, pos2):
    t = l[pos1]
    l.pop(pos1)
    l.insert(pos2, t)
    return l
    
 # Return ['R', 'R', 'R', 'G', 'G', 'B', 'B'] 
in1 = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(Solution(in1))

# Return ['R', 'R', 'R', 'G', 'G', 'G', 'B', 'B', 'B']
in1 = ['G','B','B','B','G','G', 'R','R','R']
print(Solution(in1))