"""
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C,
replace the color of the given pixel and all adjacent same colored pixels with C.

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
def Solution(ar, pixelLoc, Colour):
    Helper(ar, ar[pixelLoc[0]][pixelLoc[1]], Colour, pixelLoc[0], pixelLoc[1])
    return ar

def Helper(ar, oldCol, newCol, x, y):
    if x < 0 or x >= len(ar[0]):
        return
    if y < 0 or y >= len(ar):
        return
    
    if ar[y][x] == oldCol:
        ar[y][x] = newCol
        Helper(ar, oldCol, newCol, x + 1, y)
        Helper(ar, oldCol, newCol, x - 1, y)
        Helper(ar, oldCol, newCol, x, y + 1)
        Helper(ar, oldCol, newCol, x, y - 1)
    return ar
    

# Return [['B', 'B', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G'], ['B', 'B', 'B']]
in1 = [['B','B','W'],
        ['W','W','W'],
        ['W','W','W'],
        ['B','B','B']]
print(Solution(in1, (2,2), 'G'))

# Return [['0', '0', '0'], ['2', '2', '0'], ['0', '0', '0'], ['0', '2', '2'], ['0', '0', '0']]
in1 = [['1','1','1'],
        ['2','2','1'],
        ['1','1','1'],
        ['1','2','2'],
        ['1','1','1']]
print(Solution(in1, (0,0), '0'))