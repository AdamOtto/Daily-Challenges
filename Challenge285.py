"""
You are given an array representing the heights of neighboring buildings on a city street,
from west to east. The city assessor would like you to write an algorithm that returns
how many of these buildings have a view of the setting sun, in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3,
since the top floors of the buildings with heights 3, 7, and 8 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?
"""

def Solution(ar):
    l = len(ar)
    highestBuilding = 0
    retVal = 0
    for i in range(0, l):
        if ar[i] > highestBuilding:
            highestBuilding = ar[i]
            retVal += 1
    return retVal


in1 = [3, 7, 8, 3, 6, 1]
print(Solution(in1))

in1 = [3, 2, 1, 8, 3, 2, 1]
print(Solution(in1))

in1 = [1, 2, 3, 4, 5, 6]
print(Solution(in1))

in1 = [5, 1, 6, 1, 7, 1, 8]
print(Solution(in1))