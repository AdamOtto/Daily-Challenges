'''
A wall consists of several rows of bricks of various integer lengths and uniform height.
Your goal is to find a vertical line going from the top to the bottom of the wall that cuts
through the fewest number of bricks. If the line goes through the edge between two bricks,
this does not count as a cut.

For example, suppose the input is as follows,
where values in each row represent the lengths of bricks in that row:

[[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]
 
The best we can we do here is to draw a line after the eighth brick,
which will only require cutting through the bricks in the third and fifth row.

Given an input consisting of brick lengths for each row such as the one above,
return the fewest number of bricks that must be cut to create a vertical line.
'''

def Solution(ar):
    l = len(ar)
    if l == 0:
        return False
    sumOfHeight = sum(ar[0])
    
    d = {}
    for i in range(0,l):
        t = 0
        if sum(ar[i]) != sumOfHeight:
            return False
        for j in range(0, len(ar[i])):
            t += ar[i][j]
            if t != sumOfHeight:
                if t not in d:
                    d[t] = 1
                else:
                    d[t] += 1
    m = 0
    for key, val in d.items():
        m = max(val, m)
    return l - m

# Return 2
in1 = [ [3, 5, 1, 1],
        [2, 3, 3, 2],
        [5, 5],
        [4, 4, 2],
        [1, 3, 3, 3],
        [1, 1, 6, 1, 1]]
print(Solution(in1))

# Return 1
in1 = [ [1,1,1,1],
        [2,2],
        [3,1],
        [1,1,1,1]]
print(Solution(in1))

# Return 0
in1 = [ [1,1,1,1],
        [2,2],
        [1,1,1,1]]
print(Solution(in1))

# Return 4
in1 = [ [4],
        [1,3],
        [3,1],
        [2,2],
        [1,1,2],
        [1,2,1],
        [2,1,1],
        [1,1,1,1]]
print(Solution(in1))