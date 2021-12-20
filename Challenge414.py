"""
You have an N by N board. Write a function that, given N, returns the number
of possible arrangements of the board where N queens can be placed on the board
without threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""

def Solution(N):
    grid = [[0 for i in range(N)] for j in range(N)]
    Helper(N, grid, 0)
    for i in range(N):
        temp = ""
        for j in range(N):
            temp += str(grid[i][j]) + " "
        print(temp)

def Helper(N, grid, col):
    if col >= N:
        return True

    for i in range(N):
        if sum(grid[i]) == 0 and checkDiag(N, grid, i, col):
            grid[i][col] = 1
            if Helper(N, grid, col + 1):
                return True
            else:
                grid[i][col] = 0
    return False

def checkDiag(N, grid, i, col):
    x = i + 1
    y = col + 1
    while x < N and y < N:
        if grid[x][y] == 1:
            return False
        x += 1
        y += 1
        
    x = i + 1
    y = col - 1
    while x < N and y >= 0:
        if grid[x][y] == 1:
            return False
        x += 1
        y -= 1
    
    x = i - 1
    y = col + 1
    while x >= 0 and y < N:
        if grid[x][y] == 1:
            return False
        x -= 1
        y += 1
    
    x = i - 1
    y = col - 1
    while x >= 0 and y >= 0:
        if grid[x][y] == 1:
            return False
        x -= 1
        y -= 1
    
    return True
    
Solution(4)
print()
Solution(6)