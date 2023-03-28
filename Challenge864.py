"""
An imminent hurricane threatens the coastal town of Codeville.
If at most two people can fit in a rescue boat, and the maximum
weight limit for a given boat is k, determine how many boats
will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80]
and a boat limit of 200, the smallest number of boats required will be three.

Assumption: k will be greater than or equal to all values in the population.
"""
def Solution(popW, k):
    ar = sorted(popW)
    retVal = 0
    curWeight = 0
    while len(ar) > 0:
        if curWeight + ar[-1] <= k:
            curWeight += ar[-1]
            ar.pop(-1)
        elif curWeight + ar[0] <= k:
            curWeight += ar[0]
            ar.pop(0)
        else:
            curWeight = 0
            retVal += 1
    
    return retVal + 1
    

# Return 3
print(Solution([100, 200, 150, 80], 200))
# Return 5
print(Solution([5, 10, 15, 20, 25, 30, 35, 40, 45], 45))
# Return 9
print(Solution([1,4,2,6,6,4,3,5,1,3,7,4,8,9,3,6,3], 10))