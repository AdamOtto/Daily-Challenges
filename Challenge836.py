"""
Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input, write a function that shuffles a deck of cards
represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""
import random


def Solution(ar):
    l = len(ar)
    for i in range(l):
        swap = random.randint(1, l) - 1
        temp = ar[i]
        ar[i] = ar[swap]
        ar[swap] = temp
    return ar

# Return a randomly shuffled deck.
cards = []
for i in range(0, 52):
    cards.append(i)
print(Solution(cards))