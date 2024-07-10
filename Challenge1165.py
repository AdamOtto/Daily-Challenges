"""
A knight is placed on a given square on an 8 x 8 chessboard.
It is then moved randomly several times, where each move is a standard knight move.
If the knight jumps off the board at any point, however, it is not allowed to jump back on.

After k moves, what is the probability that the knight remains on the board?
"""
# k: number of moves, x: x location on the board, y: y location on the board
def Solution(k, x, y):
    dx = [1,-1,2,2,-1,1,-2,-2]
    dy = [2,2,1,-1,-2,-2,-1,1]

    ar = [[[0 for i in range(0, 8)]
            for j in range(0, 8)]
            for s in range(k + 1)]
    
    for i in range(0,8):
        for j in range(0,8):
            ar[0][i][j] = 1
    
    for s in range(1, k + 1):
        for i in range(8):
            for j in range(8):
                prob = 0.0
                for h in range(8):
                    di = i + dx[h]
                    dj = j + dy[h]
                    if inBounds(di, dj):
                        prob += ar[s-1][di][dj] / 8.0
                ar[s][i][j] = prob
    return ar[k][x][y]
    
def inBounds(i,j):
    if i < 0:
        return False
    if i >= 8:
        return False
    if j < 0:
        return False
    if j >= 8:
        return False
    return True

# Return 0.25
print(Solution(1, 0, 0))

# Return 0.125
print(Solution(3, 0, 0))

# Return 0.125
print(Solution(3, 7, 7))

# Return ~= 0.6
print(Solution(3, 3, 3))