"""
An imminent hurricane threatens the coastal town of Codeville.
If at most two people can fit in a rescue boat,
and the maximum weight limit for a given boat is k,
determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200,
the smallest number of boats required will be three.
"""


def Solution(pop, k):
    pop = sorted(pop)
    boats = []
    l = len(pop)

    while l > 0:
        j = l - 1
        while j > 0:
            if pop[0] + pop[j] <= k:
                boats.append( (pop.pop(0), pop.pop(j - 1)) )
                break
            j -= 1
        if j == 0:
            if pop[j] <= k:
                boats.append( pop.pop(0) )
            else:
                return False
            
        l = len(pop)
    #print(boats)
    return len(boats)

# Returns 3
pop = [100, 200, 150, 80]
k = 200
print(Solution(pop, k))

# Returns 4
pop = [1, 2, 3, 3, 4, 5, 6]
k = 6
print(Solution(pop, k))

# Returns False
pop = [2, 4, 6, 8, 10]
k = 9
print(Solution(pop, k))