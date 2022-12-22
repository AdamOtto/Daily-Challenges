"""
Alice wants to join her school's Probability Student Club.
Membership dues are computed via one of two simple probabilistic games.
The first game: roll a die repeatedly.
Stop rolling once you get a five followed by a six.
Your number of rolls is the amount you pay, in dollars.
The second game: same, except that the stopping
condition is a five followed by a five.
Which of the two games should Alice elect to play?
Does it even matter? Write a program to simulate
the two games and calculate their expected value.
# Answer: Game 1.  If Alice rolls a 5, theres a 1/6 chance she'll roll another five or a six.
If she rolls a 5 again, then she's still in the same position she was in before, so she still has a 1/6 chance of ending the game.
Game 2 doesn't have this slight advantage.
"""
import random as r

def Game1():
    cur = r.randint(1,6)
    prev = cur
    cur = r.randint(1,6)
    count = 2
    while True:
        if prev == 5 and cur == 6:
            return count
        prev = cur
        cur = r.randint(1,6)
        count += 1

def Game2():
    cur = r.randint(1, 6)
    prev = cur
    cur = r.randint(1, 6)
    count = 2
    while True:
        if prev == 5 and cur == 5:
            return count
        prev = cur
        cur = r.randint(1,6)
        count += 1

tests = 10000
g1 = 0
g2 = 0
for i in range(tests):
    g1 += Game1()
for i in range(tests):
    g2 += Game2()
# Averate is usually around 36
print("Average for game 1: " + str(g1 / tests))
# Averate is usually around 42
print("Average for game 2: " + str(g2 / tests))