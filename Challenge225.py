"""
There are N prisoners standing in a circle, waiting to be executed.
The executions are carried out starting with the kth person, and removing every
successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner
should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions
would be [2, 4, 1, 5, 3], so you should return 3.
"""

def Solution(N, k):
    count = -1
    prisoners = [i + 1 for i in range(N)]
    retVal = []

    for i in range(N):
        count += k
        if count >= len(prisoners):
            count = min( count - len(prisoners), len(prisoners) - 1)
        retVal.append(prisoners.pop(count))
        count -= 1
    return retVal

N = 5
k = 2
print(Solution(N,k))
N = 100
k = 15
print(Solution(N,k))