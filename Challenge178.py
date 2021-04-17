"""
Alice wants to join her school's Probability Student Club.
Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly.
Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter?
Write a program to simulate the two games and calculate their expected value.
"""

# Prediction: There wont be a big difference between the two games after running a simulation of each close to 100000 times.
# Results: Game 1 ends on average at around 36 rolls, and game 2 ends at 42 rolls.
# Reason: In game 1, if Alice rolls a 5, there is a 1/6 chance she rolls another 5 putting her at only 1 roll away from winning.
# In game 2, if Alice rolls a 5, she has a 1/6 chance of winning but if she fails she needs to roll a five again.
# Because of this difference, game 1 has slightly higher odds of finishing early.

import random as r

def GameOne():
    cur = r.randint(1,6)
    prev = cur
    cur = r.randint(1,6)
    count = 2
    while True:
        #print("Game1 count:" + str(count) + " - cur = " + str(cur) + ", prev = " + str(prev))
        if prev == 5 and cur == 6:
            return count
        prev = cur
        cur = r.randint(1,6)
        count += 1

def GameTwo():
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


avg1 = 0
avg2 = 0
l = 100000
for i in range(0, l):
    avg1 += GameOne()
    avg2 += GameTwo()
avg1 = avg1 / l
avg2 = avg2 / l
print("Average of " + str(l) + " instances of game 1: " + str(avg1))
print("Average of " + str(l) + " instances of game 2: " + str(avg2))