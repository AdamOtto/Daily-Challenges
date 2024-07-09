"""
You have n fair coins and you flip them all at the same time.
Any that come up tails you set aside. The ones that come up heads you flip again.
How many rounds do you expect to play before only one coin remains?
"""
import random as rand

def Solution(ar):
    t = 0
    coins = ar
    retVal = []
    for a in range(50):
        while coins > 1:
            t += 1
            remove = 0
            for i in range(coins):
                temp = rand.randint(0, 1)
                if temp == 1:
                    remove += 1
            coins -= remove
        coins = ar
        retVal.append(t)
        t = 0
        
    return sum(retVal) / len(retVal) 

# Return around 2.5 to 3
print(Solution(8))

# Return around 6.5
print(Solution(100))