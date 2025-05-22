"""
Given an integer n and a list of integers l,
write a function that randomly generates a number
from 0 to n-1 that isn't in l (uniform).
"""
import random as r

def Solution(n, l):
    temp = r.randint(0, n - 1)
    while temp in l:
        temp = r.randint(0, n - 1)
    return temp

# Return 0,2,4,5,6,8,9 uniformly
d = {}
for i in range(100):
    t = Solution(10, [1,3,7])
    if t not in d:
        d[t] = 0
    d[t] += 1

for key, val in d.items():
    print(str(key) + ": " + str(val))