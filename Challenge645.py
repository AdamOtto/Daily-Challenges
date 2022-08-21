"""
Given a 2D matrix of characters and a target word,
write a function that returns whether the word can be
found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true,
since it's the leftmost column. Similarly, given the target word 'MASS',
you should return true, since it's the last row.
"""

def Solution(in1, target):
    ly = len(in1)
    lx = len(in1[0])
    
    for y in range(ly):
        for x in range(lx):
            if in1[y][x] is target[0]:
                d = lookDown(in1, target, x, y)
                r = lookRight(in1, target, x, y)
                if d or r:
                    return True
    return False

def lookDown(grid, target, x, y):
    ly = len(in1)
    lx = len(in1[0])
    
    for i in range(1, len(target)):
        if y + i < ly:
            if grid[y+i][x] is not target[i]:
                return False
        else:
            return False
    return True
    
def lookRight(grid, target, x, y):
    ly = len(in1)
    lx = len(in1[0])
    
    for i in range(1, len(target)):
        if x + i < lx:
            if grid[y][x+i] is not target[i]:
                return False
        else:
            return False
    return True


in1 = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
 
# Return True
print(Solution(in1, "FOAM"))
# Return True
print(Solution(in1, "MASS"))
# Return False
print(Solution(in1, "NOPE"))