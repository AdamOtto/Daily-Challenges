"""
A group of houses is connected to the main water plant by means of a set of pipes.
A house can either be connected by a set of pipes extending directly to the plant,
or indirectly by a pipe to a nearby house which is otherwise connected.

For example, here is a possible configuration,
where A, B, and C are houses, and arrows represent pipes:

A <--> B <--> C <--> plant
Each pipe has an associated cost, which the utility company would like to minimize.
Given an undirected graph of pipe connections, return the lowest cost configuration
of pipes such that each house has access to water.

In the following setup, for example, we can remove all but the pipes
from plant to A, plant to B, and B to C, for a total cost of 16.

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
"""
import sys

def Solution(pipes):
    distances = {}
    for key, val in pipes.items():
        if key != 'plant':
            distances[key] = sys.maxsize
    #print(distances)
    getDistances('plant', pipes, distances)
    print(distances)
    retVal = 0
    for key, val in distances.items():
        retVal += val
    return retVal


def getDistances(cur, pipes, distances):
    temp = []
    for key, val in pipes[cur].items():
        temp.append( (key, val) )
    temp.sort(key=lambda x:x[1] )
    #print(temp)
    for val in temp:
        if val[1] < distances[val[0]]:
            distances[val[0]] = val[1]
            getDistances(val[0], pipes, distances)
    return



# Return 16
pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
print(Solution(pipes))

# Return 21
#
#       plant
#     1/    5\
#     A       B
#           9/ 1\
#           C    D
#         5/
#         E 
pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 10},
    'A': {'C':10, 'D':5, 'E':10},
    'B': {'C':9, 'D':1, 'E':15},
    'C': {'E':5},
    'D': {'E':20},
    'E': {}
}
print(Solution(pipes))
