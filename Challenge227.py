"""
Boggle is a game played on a 4 x 4 grid of letters.
The goal is to find as many words as possible that can be formed by a sequence
of adjacent letters in the grid, using each cell at most once.
Given a game board and a dictionary of valid words, implement a Boggle solver.
"""

def Solution(board, words):
    d = {}
    for y in range(0, len(board)):
        for x in range(0,len(board[y])):
            if board[y][x] not in d:
                d[board[y][x]] = []
            d[board[y][x]].append( (y,x) )
    retVal = []
    for word in words:
        if word[0] in d:
            for locations in d[word[0]]:
                prevCells = []
                prevCells.append(locations)
                if Helper(board, locations, word, 1, prevCells):
                    retVal.append(word)
                    break
    return retVal


def Helper(board, cur, word, next, prevCells):
    if next >= len(word):
        return True

    NextCells = PossibleNextCells(cur, prevCells)
    for cell in NextCells:
        if board[cell[0]][cell[1]] == word[next]:
            temp = prevCells
            temp.append(cell)
            if Helper(board, cell, word, next + 1, temp):
                return True
    return False


def PossibleNextCells(cur, prevCells):
    retVal = []
    retVal.append((cur[0]-1, cur[1]-1))
    retVal.append((cur[0]-1, cur[1]))
    retVal.append((cur[0], cur[1]-1))
    retVal.append((cur[0]-1, cur[1]+1))
    retVal.append((cur[0]+1, cur[1]-1))
    retVal.append((cur[0]+1, cur[1]))
    retVal.append((cur[0], cur[1]+1))
    retVal.append((cur[0]+1, cur[1]+1))
    i = 0
    while i < len(retVal):
        if retVal[i][0] < 0 or retVal[i][0] >= 4:
            retVal.pop(i)
            continue
        elif retVal[i][1] < 0 or retVal[i][1] >= 4:
            retVal.pop(i)
            continue
        elif retVal[i] in prevCells:
            retVal.pop(i)
            continue
        i += 1
    return retVal

in1 = [ ['t', 'e', 's', 't'],
        ['e', 'y', 'l', 'q'],
        ['s', 'a', 't', 'l'],
        ['t', 'o', 'r', 'z']]
in2 = ['test', 'ear', 'say', 'tar', 'soar', 'sat', 'yell', 'sora', 'rot', 'loss', 'meat', 'good', 'world', 'molt', 'zip', 'sas', 'tot', 'roar']
print(Solution(in1,in2))

