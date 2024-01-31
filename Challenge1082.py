"""
Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6
vertically suspended grid. The game ends either when one player creates a line of four
consecutive discs of their color (horizontally, vertically, or diagonally),
or when there are no more spots left in the grid.

Design and implement Connect 4.
"""
def printBoard(board):
    s = ""
    l = len(board)
    l2 = len(board[0])
    print("1 2 3 4 5 6 7")
    for i in range(l):
        for j in range(l2):
            s += str(board[i][j]) + " "
        print(s)
        s = ""

def AddDisc(board, col, player):
    l = len(board)
    for i in reversed(range(l)):
        if board[i][col - 1] == 0:
            board[i][col - 1] = player
            return True
    return False

def Check(board, x, y, dx, dy, player):
    #xx = x + dx
    #yy = y + dy
    if (x + dx < 0 or x + dx >= 6):
        return 0
    elif (y + dy < 0 or y + dy >= 7):
        return 0
    if board[x + dx][y + dy] == player:
        return 1 + Check(board, x + dx, y + dy, dx, dy, player)
    else:
        return 0

def winCondition(board, player, col):
    if col == -1:
        return False
    l = len(board)
    row = 0
    for i in reversed(range(1, l)):
        if board[i][col] == 0:
            row = i + 1
            break
    #t1 = Check(board, row, col, 0, 1, player)
    #t2 = Check(board, row, col, 0, -1, player)
    if Check(board, row, col, 0, 1, player) + Check(board, row, col, 0, -1, player) + 1 >= 4:
        return True
    elif Check(board, row, col, 1, 0, player) + Check(board, row, col, -1, 0, player) + 1 >= 4:
        return True
    elif Check(board, row, col, 1, 1, player) + Check(board, row, col, -1, -1, player) + 1 >= 4:
        return True
    elif Check(board, row, col, 1, -1, player) + Check(board, row, col, -1, 1, player) + 1 >= 4:
        return True

    return False

def ConnectFour():
    turns = 0
    player = (1,2)
    currentPlayer = 1
    board = []
    col = 0
    for i in range(6):
        board.append([0] * 7)

    while True:
        printBoard(board)
        col = int(input("Connect 4, it is player " + str(currentPlayer) + "'s turn.  Select the column you'd like to place a disc:"))
        if col < 1 or col > 7:
            print("Input is out of range or invalid, please try again.")
        elif not AddDisc(board, col, currentPlayer):
            print(" */\* That row is full, please select another row. */\* ")
        else:
            if winCondition(board, currentPlayer, col - 1):
                print("Player " + str(currentPlayer) + " wins!")
                printBoard(board)
                return
            if currentPlayer == 1:
                currentPlayer = 2
            else:
                currentPlayer = 1
            print()
        turns += 1
        if turns >= 6*7:
            print("Game Over")
            printBoard(board)
            return

ConnectFour()