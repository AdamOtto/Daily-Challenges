'''
A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
'''
def printGrid(grid):
    for i in range(len(grid)):
        print(grid[i])

def Solution(N):
    grid = [-1] * N
    for i in range(N):
        grid[i] = [-1] * N
    grid[0][0] = 0
    kMoveX = [2, 1, -1, -2, -2, -1, 1, 2] 
    kMoveY = [1, 2, 2, 1, -1, -2, -2, -1]
    
    if helper(N, grid, 0, 0, kMoveX, kMoveY, 1):
        printGrid(grid)
    else:
        print("Solution doesn't exist")
    
def helper(N, grid, x, y, kMoveX, kMoveY, moves):
    if moves == N*N:
        return True
        
    for i in range(8):
        new_x = x + kMoveX[i] 
        new_y = y + kMoveY[i]
        if(new_x >= 0 and new_y >= 0 and new_x < N and new_y < N and grid[new_x][new_y] == -1):
            grid[new_x][new_y] = moves
            if helper(N, grid, new_x, new_y, kMoveX, kMoveY, moves+1):
                return True
            grid[new_x][new_y] = -1
    return False
    

Solution(5)