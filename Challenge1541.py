"""
Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.
"""
import random as r
def Solution():
    deck = list(range(0, 52))
    for i in reversed(range(0, 52)):
        j = r.randint(0,i)
        swap(deck, i, j)
        print("Test")
    return deck

def swap(in1,i,j):
    t = in1[i]
    in1[i] = in1[j]
    in1[j] = t
    return

print(Solution())