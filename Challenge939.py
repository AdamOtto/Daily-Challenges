"""
Given a N by M matrix of numbers,
print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""

def Solution(in1):
    N = len(in1)
    M = len(in1[0])
    goRight(in1, 0, 0, N, M)
    
    
def goRight(in1, x, y, N, M):
    if x >= M or in1[y][x] is None:
        return
    
    finalX = M - 1
    for i in range(x, M):
        if in1[y][i] is not None:
            print(in1[y][i])
            in1[y][i] = None
        else:
            finalX = i - 1
            break
    goDown(in1, finalX, y + 1, N, M)
    
def goDown(in1, x, y, N, M):
    if y >= N or in1[y][x] is None:
        return
    
    finalY = N - 1
    for i in range(y, N):
        if in1[i][x] is not None:
            print(in1[i][x])
            in1[i][x] = None
        else:
            finalY = i - 1
            break
    goLeft(in1, x - 1, finalY, N, M)
    
    
def goLeft(in1, x, y, N, M):
    if x < 0 or in1[y][x] is None:
        return
    finalX = 0
    for i in reversed(range(0, x + 1)):
        if in1[y][i] is not None:
            print(in1[y][i])
            in1[y][i] = None
        else:
            finalX = i + 1
            break
    goUp(in1, finalX, y - 1, N, M)
    
def goUp(in1, x, y, N, M):
    if y < 0 or in1[y][x] is None:
        return
    finalY = 0
    for i in reversed(range(0, y + 1)):
        if in1[i][x] is not None:
            print(in1[i][x])
            in1[i][x] = None
        else:
            finalY = i + 1
            break
    goRight(in1, x + 1, finalY, N, M)

# Return answer from example.
Solution([[1,  2,  3,  4,  5], [6,  7,  8,  9,  10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
# Return 1 2 3 6 9 8 7 4 5
Solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]])