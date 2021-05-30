"""
In front of you is a row of N coins, with values v1, v1, ..., vn.

You are asked to play the following game. You and an opponent take turns choosing either
the first or last coin from the row, removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty,
if you move first, assuming your opponent plays optimally.
"""

def Solution(ar):
    ar = sorted(ar)
    #print(ar)
    player = []
    opponent = []
    playerTurn = True
    while len(ar) != 0:
        if playerTurn:
            player.append(ar.pop())
            playerTurn = False
        else:
            opponent.append((ar.pop()))
            playerTurn = True
    return sum(player)


in1 = [1,2,3,4,0]
print(Solution(in1))
in1 = [ 8, 15, 3, 7 ]
print(Solution(in1))
in1 = [ 2, 2, 2, 2 ]
print(Solution(in1))
in1 = [ 20, 30, 2, 2, 2, 10]
print(Solution(in1))