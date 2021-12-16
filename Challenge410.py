"""
You are given an array X of floating-point numbers x1, x2, ... xn.
These can be rounded up or down to create a corresponding array Y of integers y1, y2, ... yn.

Write an algorithm that finds an appropriate Y array with the following properties:

- The rounded sums of both arrays should be equal.
- The absolute pairwise difference between elements is minimized.
    In other words, |x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.

For example, suppose your input is [1.3, 2.3, 4.4].
In this case you cannot do better than [1, 2, 5], which has an
absolute difference of |1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1.
"""
import math

def Solution(ar):
    l = len(ar)
    arSum = int(sum(ar))
    decVals = []
    arcpy = []
    arcpy.extend(ar)
    # Floor all numbers and keep track of their decimal value.
    for i in range(0, l):
        decVals.append( (i, arcpy[i] - math.floor(arcpy[i])) )
        arcpy[i] = math.floor(arcpy[i])
    # Sort decVals based on which numbers are closer to their ceiling
    decVals = sorted(decVals, key=lambda x: x[1])
    
    # Raise numbers closer to their ceiling until we reach the rounded sum of the original list.
    while sum(arcpy) < arSum and len(decVals) > 0:
        temp = decVals.pop()
        arcpy[temp[0]] = math.ceil(ar[temp[0]])
    
    # Pairwise difference
    retVal = 0
    for i in range(l):
        retVal += abs(ar[i] - arcpy[i])
    
    return arcpy, retVal

   
print(Solution([1.3, 2.3, 4.4]))
print(Solution([1.1, 2.2, 4.4, 3.3, 5.5, 10.1, 20.2, 9.9]))