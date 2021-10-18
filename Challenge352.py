"""
A typical American-style crossword puzzle grid is an N x N matrix with black and white squares,
which obeys the following rules:

- No word can be fewer than three letters long.
- Every white square must be reachable from every other white square.
- The grid is rotationally symmetric (for example, the colors of the top left and bottom right squares must match).

Write a program to determine whether a given matrix qualifies as a crossword grid.
"""

def Solution(ar):
    N = len(ar)
    
    # Every white square must be reachable from every other white square.
    visited = [[False for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if ar[i][j] == 1:
                VisitHelper(i, j, visited, ar, N - 1)
                break
        if visited[i][j]:
            break
    
    for i in range(N):
        for j in range(N):
            if ar[i][j] == 1 and not visited[i][j]:
                return False
                
    # No word can be fewer than three letters long.
    visited = [[False for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if ar[i][j] == 1:
                if acrossHelper(i, j, ar, N) < 3 and downHelper(i, j, ar, N) < 3:
                    return False
    
    # Grid is rotationally symmetric
    for i in range(N):
        for j in range(N):
            opi = abs(N - i - 1)
            opj = abs(N - j - 1)
            if ar[i][j] != ar[opi][opj]:
                return False
    
    return True

def VisitHelper(i,j,visited, board, N):
    if board[i][j] == 1 and not visited[i][j]:
        visited[i][j] = True
        
        VisitHelper(max(0, i - 1), j, visited, board, N)
        VisitHelper(min(N, i + 1), j, visited, board, N)
        VisitHelper(i, max(0, j - 1), visited, board, N)
        VisitHelper(i, min(N, j + 1), visited, board, N)
    return

def acrossHelper(i,j, board, N):
    if board[i][j] == 1:
        count = 1
        for k in range(j + 1, N):
            if board[i][k] == 0:
                break
            count += 1
        for k in reversed(range(0, j)):
            if board[i][k] == 0:
                break
            count += 1
        return count
    return 0

def downHelper(i,j, board, N):
    if board[i][j] == 1:
        count = 1
        for k in range(i + 1, N):
            if board[k][j] == 0:
                break
            count += 1
        for k in reversed(range(0, i)):
            if board[k][j] == 0:
                break
            count += 1
        return count
    return 0


ar = [[0,1,1,1,0],
      [0,0,1,0,0],
      [1,1,1,1,1],
      [0,0,1,0,0],
      [0,1,1,1,0]]
print(Solution(ar))