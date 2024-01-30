"""
Given a 2-D matrix representing an image, a location of a pixel in
the screen and a color C, replace the color of the given pixel and
all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B
Becomes

B B G
G G G
G G G
B B B
"""

def Solution(grid, loc, col):
    g = grid.copy()
    prevCol = grid[loc[0]][loc[1]]
    Helper(grid, g, loc, prevCol, col)
    for i in range(len(g)):
        print(g[i])
    return g
    
def Helper(grid, g, cur, col, NewCol):
    if cur[0] >= len(grid) or cur[1] >= len(grid[0]):
        return
    if cur[0] < 0 or cur[1] < 0:
        return
    
    if grid[cur[0]][cur[1]] == col and g[cur[0]][cur[1]] != NewCol:
        g[cur[0]][cur[1]] = NewCol
    else:
        return
    
    Helper(grid, g, (cur[0], cur[1] + 1), col, NewCol)
    Helper(grid, g, (cur[0], cur[1] - 1), col, NewCol)
    Helper(grid, g, (cur[0] + 1, cur[1]), col, NewCol)
    Helper(grid, g, (cur[0] - 1, cur[1]), col, NewCol)
    return

# Return [['B', 'B', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G'], ['B', 'B', 'B']]
in1 = [['B', 'B', 'W'],
['W', 'W', 'W'],
['W', 'W', 'W'],
['B', 'B', 'B']]
Solution(in1, (2,2), 'G')