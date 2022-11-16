"""
An imminent hurricane threatens the coastal town of Codeville.
If at most two people can fit in a rescue boat, and the maximum weight
limit for a given boat is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80]
and a boat limit of 200, the smallest number of boats required will be three.
"""
def Solution(weights, limit):
    l = len(weights)
    arSor = sorted(weights)
    low = 0
    high = l - 1
    boats = 0
    while low < high:
        if arSor[low] + arSor[high] <= limit:
            boats += 1
            low += 1
            high -= 1
        elif arSor[high] <= limit:
            boats += 1
            high -= 1
        else:
            return False
    return boats

# Return 3
print(Solution([100, 200, 150, 80], 200))

# Return 5
print(Solution([1, 4, 5, 5, 6, 3, 2, 7, 8, 9], 10))

# Return False
print(Solution([1, 4, 5, 5, 6, 3, 2, 7, 8, 9, 11], 10))