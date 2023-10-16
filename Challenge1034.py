"""
You have n fair coins and you flip them all at the same time.
Any that come up tails you set aside.
The ones that come up heads you flip again.
How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number
of rounds you'd expect to play until one coin remains.
"""
import random as r
import math

# Returns expected vs simulated
def Solution(N):
    ar = N
    count = 0
    expected = N
    counte = 0
    
    while expected > 1:
        expected = math.floor(expected / 2)
        counte += 1
    
    while ar > 1:
        sub = 0
        for i in range(ar):
            if r.randint(0, 1) == 1:
                sub += 1
        ar -= sub
        count += 1
    return counte, count

# Return (3, 3~4)
print(Solution(10))
# Return (6, 4~7)
print(Solution(120))
# Return (2, 2~3)
print(Solution(4))
# Return (5, 4~6)
print(Solution(50))