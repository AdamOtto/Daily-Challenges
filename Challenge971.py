"""
Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?
"""
def Solution(in1):
    N = len(in1)
    for x in range(0, int(N / 2)):
        for y in range(x, N - x - 1):
            t = in1[N - 1 - y][x]
            in1[N - 1 - y][x] = in1[N - 1 - x][N - 1 - y]
            in1[N - 1 - x][N - 1 - y] = in1[y][N - 1 - x]
            in1[y][N - 1 - x] = in1[x][y]
            in1[x][y] = t

def displayMatrix(in1):
    N = len(in1)
    for i in range(0, N):
        for j in range(0, N):
            print(in1[i][j], end=' ')
        print("")
    print("")


in1 = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
displayMatrix(in1)
Solution(in1)
displayMatrix(in1)

in1 = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
displayMatrix(in1)
Solution(in1)
displayMatrix(in1)