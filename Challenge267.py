'''
You are presented with an 8 by 8 matrix representing the positions
of pieces on a chess board. The only pieces on the board are the
black king and various white pieces.
Given this matrix, determine whether the king is in check.

For details on how each piece moves, see here.

For example, given the following matrix:

...K....
........
.B......
......P.
.......R
..N.....
........
.....Q..
You should return True, since the bishop is attacking the king diagonally.

'''

def Solution(ar):
    l1 = len(ar)
    if l1 != 8:
        return False
    l2 = len(ar)
    if l2 != 8:
        return False
    king = None
    board = []
    for i in range(0, 8):
        board.append([0] * 8)
    
    for i in range(0, 8):
        for j in range(0, 8):
            if ar[i][j] == ".":
                continue
            elif ar[i][j] == "K":
                king = (i, j)
            elif ar[i][j] == "B":
                #Determine all spaces bishop can reach
                setBoardBishop(board, ar, i, j)
            elif ar[i][j] == "R":
                #Determine all spaces rook can reach
                setBoardRook(board, ar, i, j)
            elif ar[i][j] == "Q":
                #Determine all spaces queen can reach
                setBoardQueen(board, ar, i, j)
            elif ar[i][j] == "P":
                #Determine all spaces pawn can reach
                setBoardPawn(board, ar, i, j)
            elif ar[i][j] == "N":
                #Determine all spaces knight can reach
                setBoardKnight(board, i, j)
            
            if king is not None:
                if board[king[0]][king[1]] == 1:
                    return True
    return False
                
def setBoardBishop(board, ar, i, j):
    setBoard(board, ar, i + 1, j + 1, 1, 1)
    setBoard(board, ar, i - 1, j + 1, -1, 1)
    setBoard(board, ar, i + 1, j - 1, 1, -1)
    setBoard(board, ar, i - 1, j - 1, -1, -1)
    return

def setBoardRook(board, ar, i, j):
    setBoard(board, ar, i, j + 1, 0, 1)
    setBoard(board, ar, i, j - 1, 0, -1)
    setBoard(board, ar, i + 1, j, 1, 0)
    setBoard(board, ar, i - 1, j, -1, 0)
    return
    
def setBoardQueen(board, ar, i, j):
    setBoardRook(board, ar, i, j)
    setBoardBishop(board, ar, i, j)
    return

def setBoardPawn(board, ar, i, j):
    if i - 1 < 0:
        return
    if j + 1 >= 8:
        return
    if j - 1 < 0:
        return
    if ar[i - 1][j + 1] == "." or ar[i - 1][j - 1] == "K":
        board[i - 1][j + 1] = 1
    if ar[i - 1][j - 1] == "." or ar[i - 1][j - 1] == "K":
        board[i - 1][j - 1] = 1
    return
    
def setBoardKnight(board, i, j):
    positions = [
        (i - 2, j + 1),
        (i - 2, j - 1),
        (i - 1, j - 2),
        (i + 1, j - 2),
        (i - 1, j + 2),
        (i + 1, j + 2),
        (i + 2, j + 1),
        (i + 2, j - 1)
        ]
    for pos in positions:
        if inRange(pos[0], pos[1]):
            board[pos[0]][pos[1]] = 1
    return

def setBoard(board, ar, i, j, deltaI, deltaJ):
    if not inRange(i, j):
        return
    if ar[i][j] == "." or ar[i][j] == "K":
        board[i][j] = 1
        setBoard(board, ar, i + deltaI, j + deltaJ, deltaI, deltaJ)
    return

def inRange(i, j):
    if i < 0 or i >= 8:
        return False
    if j < 0 or j >= 8:
        return  False
    return True

#[".",".",".",".",".",".",".","."]
# Should return true, based on example given.
in1 = [
    [".",".",".","K",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".","B",".",".",".",".",".","."],
    [".",".",".",".",".",".","P","."],
    [".",".",".",".",".",".",".","R"],
    [".",".","N",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".","Q",".","."]
    ]
print(Solution(in1))

# Should return false, other pieces are blocking check.
in1 = [
    [".","Q",".",".",".",".",".","B"],
    [".",".",".",".",".",".",".","."],
    [".",".",".","R",".","P",".","."],
    [".",".",".",".","K",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".","N",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".","R",".",".","."]
    ]
print(Solution(in1))