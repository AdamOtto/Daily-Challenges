"""
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null.
You can move up, left, down, and right. You cannot move through walls.
You cannot wrap around the edges of the board.
"""

def Solve(maze, start, end):
    steps = []
    for y in range(0, len(maze)):
        steps.append([])
        for x in range(0, len(maze[0])):
            steps[y].append(0)
    #steps = [[0]*len(maze)]*len(maze[0])
    #print(start)
    steps[start[0]][start[1]] = 1
    #print(steps)
    neigh = getNeighboors(maze, steps, start)
    #print(neigh)
    for x in neigh:
        steps[x[0]][x[1]] = steps[start[0]][start[1]] + 1
    #print(steps)
    for x in neigh:
        SolveHelper(maze, x, end, steps)

def SolveHelper(maze, cur, end, steps):
    if cur == end:
        print(str(steps[cur[0]][cur[1]] - 1))
        print(steps)
    neigh = getNeighboors(maze, steps, cur)
    for x in neigh:
        steps[x[0]][x[1]] = steps[cur[0]][cur[1]] + 1
    #print(steps)
    for x in neigh:
        SolveHelper(maze, x, end, steps)

def getNeighboors(maze, steps, loc):
    retVal = []
    if loc[0] - 1 >= 0 and maze[loc[0] - 1][loc[1]] is False and steps[loc[0] - 1][loc[1]] == 0:
        retVal.append( (loc[0] - 1, loc[1]) )
        
    if loc[0] + 1 < len(maze) and maze[loc[0] + 1][loc[1]] is False and steps[loc[0] + 1][loc[1]] == 0:
        retVal.append( (loc[0] + 1, loc[1]) )
    
    if loc[1] - 1 >= 0 and maze[loc[0]][loc[1] - 1] is False and steps[loc[0]][loc[1] - 1] == 0:
        retVal.append( (loc[0], loc[1] - 1) )
    if loc[1] + 1 < len(maze[0]) and maze[loc[0]][loc[1] + 1] is False and steps[loc[0]][loc[1] + 1] == 0:
        retVal.append( (loc[0], loc[1] + 1) )
    return retVal
    
in1 = [[False, False, False, False],
[True, True, False, True],
[False, False, False, False],
[False, False, False, False]]

start = (3,0)
end = (0,0)
Solve(in1, start, end)