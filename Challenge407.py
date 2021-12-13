"""
A group of houses is connected to the main water plant by means of a set of pipes.
A house can either be connected by a set of pipes extending directly to the plant,
or indirectly by a pipe to a nearby house which is otherwise connected.

For example, here is a possible configuration,
where A, B, and C are houses, and arrows represent pipes:

A <--> B <--> C <--> plant
Each pipe has an associated cost, which the utility company would like to minimize.
Given an undirected graph of pipe connections, return the lowest cost configuration of
pipes such that each house has access to water.

In the following setup, for example, we can remove all but the pipes from plant to A,
plant to B, and B to C, for a total cost of 16.

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
"""
import sys

def Solution(ar):
    lowestCosts = ar['plant'].copy()
    for key, val in lowestCosts.items():
        lowestCosts[key] = sys.maxsize
    Helper(ar, 'plant', lowestCosts)
    retVal = sum(lowestCosts.values())
    return retVal, lowestCosts

def Helper(ar, cur, lowestCosts):
    t = ar[cur].copy()
    while len(t) > 0:
        lowestVal = min(t, key=t.get)
        if t[lowestVal] < lowestCosts[lowestVal]:
            lowestCosts[lowestVal] = t[lowestVal]
            Helper(ar, lowestVal, lowestCosts)
        t.pop(lowestVal)


# Return 16
pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
print(Solution(pipes))

# Return 25
pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20, 'D':30},
    'A': {'C': 15, 'B': 4},
    'B': {'C': 10, 'D': 15},
    'C': {'D': 10},
    'D': {}
}
print(Solution(pipes))