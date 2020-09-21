'''
There is an N by M matrix of zeroes.
Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner.
You can only move right or down.
'''

def TotalPaths(m,n):
    
    grid = [0] * n
    for i in range(n):
        grid[i] = [0]*m
    for x in range(m):
        grid[0][x] = 1
    for y in range(n):
        grid[y][0] = 1
    
    for x in range(1,m):
        for y in range(1,n):
            grid[y][x] = grid[y - 1][x] + grid[y][x-1]
    print(grid[n-1][m-1])
    
TotalPaths(5,5)