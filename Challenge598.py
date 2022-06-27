"""
You have n fair coins and you flip them all at the same time.
Any that come up tails you set aside.
The ones that come up heads you flip again.
How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number
of rounds you'd expect to play until one coin remains.
"""
import random as r

def Solution(N):
    ar = N
    count = 0
    while ar > 1:
        sub = 0
        for i in range(ar):
            if r.randint(0, 1) == 1:
                sub += 1
        ar -= sub
        count += 1
    return count


print(Solution(10))
print(Solution(120))
print(Solution(4))
print(Solution(50))