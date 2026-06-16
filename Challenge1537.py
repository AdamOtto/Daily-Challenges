"""
You are given a starting state start,
a list of transition probabilities for a Markov chain,
and a number of steps num_steps.
Run the Markov chain starting from start for num_steps and compute
the number of times we visited each state.

For example, given the starting state a, number of steps 5000,
and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
"""

import random as r

def Solution(startingState, steps, markov):
    curState = startingState
    retVal = {}

    for key, val in markov.items():
        retVal[key] = 0

    for i in range(0, steps):
        rand = r.random()
        for state in markov[curState]:
            rand -= state[1]
            if rand <= 0:
                curState = state[0]
                break
        retVal[curState] += 1

    return retVal

# Possible return: {'a': 3123, 'b': 1529, 'c': 348}
markov = [
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
d = {}
for i in markov:
    if i[0] not in d:
        d[i[0]] = []
        d[i[0]].append( (i[1], i[2]) )
    else:
        d[i[0]].append((i[1], i[2]))

print(Solution("a", 5000, d))