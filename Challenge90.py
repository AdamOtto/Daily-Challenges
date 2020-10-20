'''
Given an integer n and a list of integers l,
write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform)
'''
import random

def Solution(n, l):
    vals = []
    for i in range(0,n):
        if i not in l:
            vals.append(i)
    
    for i in reversed(range(0,len(vals))):
        t = random.randrange(len(vals))
        t2 = vals[t]
        vals[t] = vals[i]
        vals[i] = t2
    
    
    print(vals)

n = 30
l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
Solution(n, l)