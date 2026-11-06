"""
Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits.
The objective is to fill the grid with the constraint that every row, column, and box
(3 by 3 subgrid) must contain all of the digits from 1 to 9

Implement an efficient sudoku solver.
"""
def Solver(d):

    grid = [None] * 9
    for i in range(0,9):
        grid[i] = [None] * 9

    for key, value in d.items():
        x = key[0]
        y = key[1]
        grid[x][y] = value
    SolverHelper(d, grid, 0, 0)


def SolverHelper(d, grid, x, y):

    if (x,y) not in d:
        for i in range(1, 10):
            grid[x][y] = i
            if check(grid, x, y):
                if x != 8:
                    SolverHelper(d, grid, x + 1, y)
                else:
                    if y != 8:
                        SolverHelper(d, grid, 0, y + 1)
                    else:
                        displaySudokuPuzzle(grid)
        grid[x][y] = None
        return
    else:
        if x != 8:
            SolverHelper(d, grid, x + 1, y)
        else:
            if y != 8:
                SolverHelper(d, grid, 0, y + 1)
            else:
                displaySudokuPuzzle(grid)
    return


def check(grid, x, y):
    d = []
    #Check y
    for i in range(0,9):
        if grid[x][i] not in d or grid[x][i] is None:
            d.append(grid[x][i])
    if len(d) != 9:
        return False

    d = []
    #Check x
    for i in range(0, 9):
        if grid[i][y] not in d or grid[i][y] is None:
            d.append(grid[i][y])
    if len(d) != 9:
        return False

    #Check grid
    gridx = []
    gridy = []
    if x >= 0 or x <= 2:
        gridx = [0, 1, 2]
    elif x >= 3 or x <= 5:
        gridx = [3, 4, 5]
    elif x >= 6 or x <= 8:
        gridx = [6, 7, 8]

    if y >= 0 or y <= 2:
        gridy = [0, 1, 2]
    elif y >= 3 or y <= 5:
        gridy = [3, 4, 5]
    elif y >= 6 or y <= 8:
        gridy = [6, 7, 8]

    d = []
    for x in gridx:
        for y in gridy:
            if grid[x][y] not in d or grid[x][y] is None:
                d.append(grid[x][y])
    if len(d) != 9:
        return False

    return True

def displaySudokuPuzzle(sud):

    for i in range(0, len(sud)):
        if i % 3 == 0 and i != 0:
            print("")
        print( str(sud[i][0]) + " " + str(sud[i][1]) + " " + str(sud[i][2]) + "\t" +
        str(sud[i][3]) + " " + str(sud[i][4]) + " " + str(sud[i][5]) + "\t" +
        str(sud[i][6]) + " " + str(sud[i][7]) + " " + str(sud[i][8]))
    print("\n")

"""
Return:
1 4 6   7 9 2   3 8 5
2 5 8   3 4 6   7 9 1
3 7 9   5 8 1   4 6 2

4 3 7   9 1 5   8 2 6
5 8 1   6 2 7   9 3 4
6 9 2   4 3 8   1 5 7

7 1 3   2 6 9   5 4 8
8 2 4   1 5 3   6 7 9
9 6 5   8 7 4   2 1 3
"""
in1 = {
    (0,0) : 1,    (0,2) : 6,    (0,5) : 2,    (0,6) : 3,
    (1,1) : 5,    (1,5) : 6,    (1,7) : 9,    (1,8) : 1,
    (2,2) : 9,    (2,3) : 5,    (2,5) : 1,    (2,6) : 4,    (2,7) : 6,    (2,8) : 2,
    (3,1) : 3,    (3,2) : 7,    (3,3) : 9,    (3,5) : 5,
    (4,0) : 5,    (4,1) : 8,    (4,2) : 1,    (4,4) : 2,    (4,5) : 7,    (4,6) : 9,
    (5,3) : 4,    (5,5) : 8,    (5,6) : 1,    (5,7) : 5,    (5,8) : 7,
    (6,3) : 2,    (6,4) : 6,    (6,6) : 5,    (6,7) : 4,
    (7,2) : 4,    (7,3) : 1,    (7,4) : 5,    (7,6) : 6,    (7,8) : 9,
    (8,0) : 9,    (8,3) : 8,    (8,4) : 7,    (8,5) : 4,    (8,6) : 2,    (8,7) : 1
}

Solver(in1)