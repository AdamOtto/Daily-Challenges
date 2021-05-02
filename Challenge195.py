"""
Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller
than M[i1, j1] and larger than M[i2, j2].
"""

# Simple Solution, O(n)
def SimpleSolution(mat, i1, i2):
    small = mat[i1[0]][i1[1]]
    large = mat[i2[0]][i2[1]]
    count = 0
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            if mat[i][j] < small or mat[i][j] > large:
                count += 1
    return count


in1 = [[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]

i1 = 1
j1 = 1
i2 = 3
j2 = 3
print(SimpleSolution(in1, (i1, j1), (i2,j2)))
