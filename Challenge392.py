"""
You are given a 2D matrix of 1s and 0s
where 1 represents land and 0 represents water.

Grid cells are connected horizontally orvertically (not diagonally).
The grid is completely surrounded by water, and there is exactly
one island (i.e., one or more connected land cells).

An island is a group of cells connected horizontally or
vertically, but not diagonally. There is guaranteed to be exactly
one island in this grid, and the island doesn't have water inside
that isn't connected to the water around the island.
Each cell has a side length of 1.

Determine the perimeter of this island.

For example, given the following matrix:
[[0, 1, 1, 0],
[1, 1, 1, 0],
[0, 1, 1, 0],
[0, 0, 1, 0]]

Return 14.
"""

# O(n)
def Solution(ar):
    x = len(ar)
    y = len(ar[0])
    retVal = 0
    for i in range(x):
        for j in range(y):
            if ar[i][j] == 1:
                retVal += CheckPerimeter(ar, i, j)
    return retVal    
    
def CheckPerimeter(ar, i, j):
    retVal = 0
    if i + 1 >= len(ar) or ar[i + 1][j] == 0:
        retVal += 1
    
    if i - 1 < 0 or ar[i - 1][j] == 0:
        retVal += 1
    
    if j + 1 >= len(ar[0]) or ar[i][j + 1] == 0:
        retVal += 1
    
    if j - 1 > len(ar[0]) or ar[i][j - 1] == 0:
        retVal += 1
    
    return retVal

# Return 14
in1 = [[0, 1, 1, 0],
[1, 1, 1, 0],
[0, 1, 1, 0],
[0, 0, 1, 0]]
print(Solution(in1))

# Return 8
in1 = [[0, 0, 0, 0],
[0, 1, 1, 0],
[0, 0, 1, 0],
[0, 0, 0, 0]]
print(Solution(in1))