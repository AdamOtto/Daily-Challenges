'''
Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input, write a function that shuffles a deck of cards represented
as an array using only swaps.

It should run in O(N) time.
'''
import random

def Solution(in1):
    l = len(in1)
    
    for i in reversed(range(0,l)):
        j = random.randint(0,i)
        swap(in1,i,j)
    print(in1)

def swap(in1,i,j):
    t = in1[i]
    in1[i] = in1[j]
    in1[j] = t
    return

in1 = [0] * 52
for i in range(0,52):
    in1[i] = i + 1
print(in1)
Solution(in1)
    
