"""
You met a 4-th dimensional being who challenged you to a game of dice.
The rules are simple: each player rolls 3 6-sided dice and takes the sum
of each combination of 2 dice.
The player with the highest sum wins.
If the first-highest sum is a tie, consider the second-highest sum, and so on.

Your opponent's dice look normal, but you think they might have more than 6 sides!
Your goal is to find out if the alien rolled a number higher
than 6 given the three sums of the three dice rolls.
"""
# O(1) solution.  True means no cheating, False means they cheated.
def Solution(ar):
    x = ((ar[0] + ar[1]) - ar[2]) / 2
    y = ar[0] - x
    z = ar[1] - x
    
    if (x in range(1, 7) and (x).is_integer()) and (y in range(1, 7) and (y).is_integer()) and (z in range(1, 7) and (z).is_integer()):
        return (True, [x, y, z])
    return (False, [x, y, z])
    
# Return True, rolled 3, 5, 6
print(Solution([8, 11, 9]))

# Return False, rolled 2, 4, 7
print(Solution([9, 11, 6]))

# Return False, rolled 4.5, 5.5, 6.5
print(Solution([10,11,12]))

# Return False, rolled 0, 1, 2
print(Solution([1,2,3]))

# Return False, rolled -0.5, 1.5, 2.5
print(Solution([1,2,4]))

# Return True, rolled 3, 3, 6
print(Solution([6,9,9]))

# Return False, rolled 1.5, 1.5, 1.5
print(Solution([3,3,3]))