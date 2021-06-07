"""
Snakes and Ladders is a game played on a 10 x 10 board,
the goal of which is get from square 1 to square 100.
On each turn players will roll a six-sided die and move forward
a number of spaces equal to the result.
If they land on a square that represents a snake or ladder,
they will be transported ahead or behind, respectively, to a new square.

Find the smallest number of turns it takes to play snakes and ladders.

For convenience, here are the squares representing snakes and ladders, and their outcomes:

snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
"""
def Solution(snake, ladder):
    cur = 0
    turns = 0
    retVal = Solver(snake, ladder, cur, turns)
    if retVal > 100:
        return False
    else:
        return retVal

def Solver(snake, ladder, cur, turns):
    if cur == 100:
        return turns

    # Find ladders
    next = []
    for i in range(cur + 1, min(101, cur + 7)):
        if i in ladder:
            next.append(ladder[i])

    # Go up ladder, finding path with least amount of turns.
    minTurns = 1000
    if len(next) > 0:
        for i in next:
            minTurns = min(minTurns, Solver(snake, ladder, i, turns + 1))

    # Alternatively, go up by 1to6 while avoiding snakes.  Whichever moves us further along.
    for i in reversed( range(cur + 1, min(101, cur + 7)) ):
        nextCur = min(100, i)
        if nextCur not in snakes:
            minTurns = min(minTurns, Solver(snake, ladder, nextCur, turns + 1))
            break
    return minTurns


snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
print(Solution(snakes, ladders))

snakes = {2:1, 3:1, 4:1, 5:1, 6:1, 7:1}
ladders = {8:100}
print(Solution(snakes, ladders))

# If program takes 4->11, will take 5 turns.  If program takes 10:25, will take 4 turns.
snakes = {}
for i in range(30, 51):
    snakes[i] = 1
ladders = { 29:95, 10:27, 4:11}
print(Solution(snakes, ladders))