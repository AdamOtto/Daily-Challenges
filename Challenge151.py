"""
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C,
replace the color of the given pixel and all adjacent same colored pixels with C.

The top left of the matrix is considered (1,1)
"""

def Solution(mat, point, colour):
    p = ( point[0] - 1, point[1] - 1)
    origCol = mat[p[0]][p[1]]
    neighboor = getNeighboorCoordinates(mat, p)
    #print(n)
    for n in neighboor:
        if mat[n[0]][n[1]] is origCol:
            mat[n[0]][n[1]] = colour
    mat[p[0]][p[1]] = colour


def getNeighboorCoordinates(mat, p):
    y = len(mat)
    x = len(mat[0])
    retVal = []
    if p[0] - 1 >= 0:
        retVal.append( (p[0] - 1, p[1]) )
    if p[1] - 1 >= 0:
        retVal.append( (p[0], p[1] - 1 ))
    if p[1] - 1 >= 0 and p[0] - 1 >= 0:
        retVal.append((p[0] - 1, p[1] - 1))
    if p[0] + 1 < y:
        retVal.append(( p[0] + 1, p[1] ))
    if p[1] + 1 < x:
        retVal.append( (p[0], p[1] + 1 ))
    if p[0] + 1 < y and p[1] + 1 < x:
        retVal.append((p[0] + 1, p[1] + 1))
    if p[0] - 1 >= 0 and p[1] + 1 < x:
        retVal.append((p[0] - 1, p[1] + 1))
    if p[0] + 1 < y and p[1] - 1 >= 0:
        retVal.append((p[0] + 1, p[1] - 1))
    return retVal

def printMat(mat):
    for i in mat:
        s = ""
        for j in i:
            s += j
        print(s)

in1 = [["B", "B", "W"],
       ["W", "W", "W"],
       ["W", "W", "W"],
       ["B", "B", "B"]]
p = (2,2)
c = "G"

printMat(in1)
print("")
Solution(in1, p, c)
printMat(in1)