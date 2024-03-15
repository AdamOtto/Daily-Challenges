"""
Consider the following scenario: there are N mice and N holes
placed at integer points along a line. Given this, find a method that maps mice
to holes such that the largest number of steps any mouse takes is minimized.

Each move consists of moving one mouse one unit to the left or right,
and only one mouse can fit inside each hole.

For example, suppose the mice are positioned at [1, 4, 9, 15],
and the holes are located at [10, -5, 0, 16].
In this case, the best pairing would require us to send the mouse at 1 to the hole at -5,
so our function should return 6.
"""
def Solution(mice, holes):
    if len(mice) != len(holes):
        return None
    l = len(mice)
    m = sorted(mice)
    h = sorted(holes)
    
    retVal = 0
    
    for i in range(l):
        retVal = max(abs(m[i] - h[i]), retVal)
    return retVal
    
# Return 6
print(Solution([1, 4, 9, 15], [10, -5, 0, 16]))

# Return 136
print(Solution([100,101,120,140,132], [0,1,2,3,4]))