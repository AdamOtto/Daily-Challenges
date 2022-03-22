"""
You are given an M by N matrix consisting of booleans
that represents a board. Each True boolean represents a wall.
Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach the end
coordinate from the start. If there is no possible path,
then return null. You can move up, left, down, and right.
You cannot move through walls.
You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left),
the minimum number of steps required to reach the end is 7,
since we would need to go through (1, 2) because there is
a wall everywhere else on the second row.
"""
import sys

def Solution(ar, start, end):
    M = len(ar)
    if M == 0:
        return None
    N = len(ar[0])
    q = []
    board = [[sys.maxsize for i in range(N)] for j in range(M)]
    board[start[0]][start[1]] = 0
    q.append((start, 0))
    while len(q) > 0:
        temp1, steps = q.pop(0)
        temp2 = getNeighbour(ar, M, N, temp1)
        for t in temp2:
            if board[t[0]][t[1]] > steps + 1:
                q.append((t, steps + 1))
                board[t[0]][t[1]] = steps + 1
    if board[end[0]][end[1]] < sys.maxsize:
        return board[end[0]][end[1]]
    return None

def getNeighbour(ar, M, N, cur):
    retVal = []
    if cur[0] - 1 >= 0 and ar[cur[0] - 1][cur[1]] is False:
        retVal.append( (cur[0] - 1, cur[1]) )
    if cur[0] + 1 < M and ar[cur[0] + 1][cur[1]] is False:
        retVal.append( (cur[0] + 1, cur[1]) )
    if cur[1] - 1 >= 0 and ar[cur[0]][cur[1] - 1] is False:
        retVal.append( (cur[0], cur[1] - 1) )
    if cur[1] + 1 < N and ar[cur[0]][cur[1] + 1] is False:
        retVal.append( (cur[0], cur[1] + 1) )
    return retVal

# Return 7
in1 = [ [False, False, False, False, False],
        [True, True, False, True, True],
        [False, False, False, False, False],
        [False, False, False, False, False]]
print(Solution(in1, (3, 0), (0, 0)))

# Return None
in1 = [[False, False, True, False, False]]
print(Solution(in1, (0, 0), (0, 4)))


# Return 16
in1 = [ [False, False, False, False, False],
        [True, True, True, True, False],
        [False, False, False, False, False],
        [False, True, True, True, True],
        [False, False, False, False, False]]
print(Solution(in1, (0, 0), (4, 4)))