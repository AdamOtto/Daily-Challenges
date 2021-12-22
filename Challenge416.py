"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.
"""

def Solution(ar):
    if len(ar) <= 1:
        return 0
    retVal = 0
    for i in range(1, len(ar)):
        stepx = abs(ar[i - 1][0] - ar[i][0])
        stepy = abs(ar[i - 1][1]- ar[i][1])
        
        if stepx < stepy:
            retVal += stepx + (stepy - stepx)
        elif stepy < stepx:
            retVal += stepy + (stepx - stepy)
        elif stepx == stepy:
            retVal += stepx
    return retVal

# Return 2
print(Solution([(0,0), (2,2)]))

# Return 5
print(Solution([(0,0), (2,2), (4,5)]))

# Return 27
print(Solution([(20,25), (15,20), (5,12), (1,4), (0,0)]))