"""
You are writing an AI for a 2D map game. You are somewhere in a 2D grid,
and there are coins strewn about over the map.

Given the position of all the coins and your current position,
find the closest coin to you in terms of Manhattan distance.
That is, you can move around up, down, left, and right, but not diagonally.
If there are multiple possible closest coins, return any of them.

For example, given the following map, where you are x, coins are o,
and empty spaces are '.' (top left is 0, 0):

---------------------
| . | . | x | . | o |
---------------------
| o | . | . | . | . |
---------------------
| o | . | . | . | o |
---------------------
| . | . | o | . | . |
---------------------
return (0, 4), since that coin is closest.
This map would be represented in our question as:

Our position: (0, 2)
Coins: [(0, 4), (1, 0), (2, 0), (3, 2)]
"""

def Solution(position, coins):
    retVal = None
    shortestPath = None
    for i in range(0, len(coins)):
        if shortestPath is None:
            shortestPath = abs(position[0] - coins[i][0]) + abs(position[1] - coins[i][1])
            retVal = coins[i]
        else:
            if abs(position[0] - coins[i][0]) + abs(position[1] - coins[i][1]) < shortestPath:
                shortestPath = abs(position[0] - coins[i][0]) + abs(position[1] - coins[i][1])
                retVal = coins[i]
    return retVal
    

in1 = (0, 2)
in2 = [(0, 4), (1, 0), (2, 0), (3, 2)]
print(Solution(in1, in2))