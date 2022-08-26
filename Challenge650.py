"""
Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller
than M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:

[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [24, 25, 30, 35, 40, 45]]
And i1 = 1, j1 = 1, i2 = 3, j2 = 3,
return 15 as there are 15 numbers in the matrix
smaller than 6 or greater than 23.
"""

def SimpleSolution(mat, i1, i2):
    small = mat[i1[0]][i1[1]]
    large = mat[i2[0]][i2[1]]
    count = 0
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            if mat[i][j] < small or mat[i][j] > large:
                count += 1
    return count

def Solution(ar, i1, i2):
    N = len(ar)
    M = len(ar[0])
    visited = set()
    retVal = 0
    retVal += FindSmalls(ar, N, M, ar[i1[0]][i1[1]], visited)
    retVal += FindLarges(ar, N, M, ar[i2[0]][i2[1]], visited)
    return retVal
    
def FindSmalls(ar, N, M, val, visited):
    q = []
    q.append( (0,0) )
    retVal = 0
    while len(q) > 0:
        cur = q.pop(0)
        if cur[0] < N and cur[1] < M and cur not in visited and ar[cur[0]][cur[1]] < val:
            retVal += 1
            visited.add( cur )
            q.append( (cur[0], cur[1] + 1) )
            q.append( (cur[0] + 1, cur[1]) )
    return retVal

def FindLarges(ar, N, M, val, visited):
    q = []
    q.append( (N - 1, M - 1) )
    retVal = 0
    while len(q) > 0:
        cur = q.pop(0)
        if cur[0] >= 0 and cur[1] >= 0 and cur not in visited and ar[cur[0]][cur[1]] > val:
            retVal += 1
            visited.add( cur )
            q.append( (cur[0], cur[1] - 1) )
            q.append( (cur[0] - 1, cur[1]) )
    return retVal

# Return 15
in1 = [[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [24, 25, 30, 35, 40, 45]]
print(Solution(in1, (1, 1), (3,3)))
print(SimpleSolution(in1, (1, 1), (3,3)))

# Return 12
print(Solution(in1, (0, 3), (2,5)))
print(SimpleSolution(in1, (0, 3), (2,5)))

# Return 29
print(Solution(in1, (0, 0), (0, 0)))
print(SimpleSolution(in1, (0, 0), (0, 0)))

# Return 30
print(Solution(in1, (3, 3), (1, 1)))
print(SimpleSolution(in1, (3, 3), (1, 1)))