"""
There is an N by M matrix of zeroes. Given N and M,
write a function to count the number of ways of starting at
the top-left corner and getting to the bottom-right corner.
You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2,
since there are two ways to get to the bottom-right
Right, then down
Down, then right

Given a 5 by 5 matrix, there are 70 ways
to get to the bottom-right.
"""

def Solution(m,n):
    
    grid = [0] * n
    for i in range(n):
        grid[i] = [0] * m
    for x in range(m):
        grid[0][x] = 1
    for y in range(n):
        grid[y][0] = 1
    
    for x in range(1,m):
        for y in range(1,n):
            grid[y][x] = grid[y - 1][x] + grid[y][x-1]
    return grid[n-1][m-1]

# Return 70
print(Solution(5,5))

# Return 1
print(Solution(1,7))

# Return 120
print(Solution(4,8))