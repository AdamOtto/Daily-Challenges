'''
The skyline of a city is composed of several buildings of various widths and heights,
possibly overlapping one another when viewed from a distance.
We can represent the buildings using an array of (left, right, height) tuples,
which tell us where on an imaginary x-axis a building begins and ends, and how tall it is.
The skyline itself can be described by a list of (x, height) tuples,
giving the locations at which the height visible to a distant observer changes, and each new height.

Given an array of buildings as described above, create a function that returns the skyline.

For example, suppose the input consists of the buildings [(0, 15, 3), (4, 11, 5), (19, 23, 4)].
In aggregate, these buildings would create a skyline that looks like the one below.

     ______  
    |      |        ___
 ___|      |___    |   | 
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------

As a result, your function should return [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)].

**Assumption based on example**
building foregound precedence is based on how late they arrive in the input array.
A < B < C
'''
import sys

def Solution(ar):
    d = {}
    skylineStart = sys.maxsize
    skylineEnd = -sys.maxsize
    
    for arg in ar:
        left = min(arg[0], arg[1])
        right = max(arg[0], arg[1])
        height = arg[2]
        
        if skylineStart > left:
            skylineStart = left
        if skylineEnd < right:
            skylineEnd = right
        
        for i in range(left, right):
            if i not in d:
                d[i] = height
            else:
                d[i] = max(height, d[i])
    
    retVal = []
    last = d[skylineStart]
    retVal.append( (skylineStart, d[skylineStart]) )
    hold = None
    for i in range(skylineStart, skylineEnd + 1):
        if i in d:
            hold = d[i]
        else:
            hold = 0
        
        if hold != last:
            retVal.append( (i, hold) )
            last = hold
    
    return retVal


in1 = [(0, 15, 3), (4, 11, 5), (19, 23, 4)]
print(Solution(in1))

in1 = [ (0,1,10), (3,4,11), (7,8,5), (5,6,10), (0,10,3) ]
print(Solution(in1))

in1 = [ (1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16), (14, 3, 25), (19, 18, 22), (23, 13, 29), (24, 4, 28) ]
print(Solution(in1))
