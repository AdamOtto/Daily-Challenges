"""
Consider the following scenario: there are N mice and N holes placed at integer points along a line.
Given this, find a method that maps mice to holes such that the largest number of steps any mouse
takes is minimized.

Each move consists of moving one mouse one unit to the left or right,
and only one mouse can fit inside each hole.

For example, suppose the mice are positioned at [1, 4, 9, 15],
and the holes are located at [10, -5, 0, 16]. In this case,
the best pairing would require us to send the mouse at 1 to the hole at -5,
so our function should return 6.
"""

def Solution(mice, hole):
    N = len(mice)
    if N != len(hole):
        return False
    mice = sorted(mice)
    hole = sorted(hole)
    
    retVal = 0
    
    for i in range(0, N):
        if abs(mice[i] - hole[i]) > retVal:
            retVal = abs(mice[i] - hole[i])
    return retVal
    

# Return 6
mice = [1, 4, 9, 15]
hole = [10, -5, 0, 16]
print(Solution(mice, hole))

# Return 99
mice = [1, 101, 202, 303]
hole = [110,300,100,200]
print(Solution(mice, hole))