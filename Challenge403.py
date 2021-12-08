"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive)
with uniform probability, implement a function rand7()
that returns an integer from 1 to 7 (inclusive).
"""
import random

def rand5():
    return random.randint(1, 5)

def rand25():
    return (5 * (rand5() - 1)) + rand5()

def rand7():
    t = 25
    while t > 7:
        t = rand25()
    return t
    
    
d = {}
for i in range(100000):
    t = rand7()
    if t not in d:
        d[t] = 0
    d[t] += 1
s = 0
for key, val in d.items():
    s += val
for key, val in d.items():
    print(str(key) + ": " + str(val / s))


