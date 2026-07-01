"""
MegaCorp wants to give bonuses to its employees based on how many
lines of codes they have written. They would like to give the smallest positive amount
to each worker consistent with the constraint that if a developer has written more lines
of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp,
determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30],
you should return [1, 2, 3, 4, 2, 1].
"""

def Solution(ar):
    l = len(ar)
    retVal = [1] * l
    localMax = 0
    localMin = 0
    for i in range(1, l):
        if ar[i] < ar[i - 1]:
            localMax = i - 1
            count = 0
            for j in range(localMin, localMax + 1):
                retVal[j] += count
                count += 1
            if localMax == localMin:
                retVal[localMax] += 1
            localMin = i

    if ar[l - 1] > ar[l - 2]:
        retVal[l - 1] += 1

    return retVal

# Return [1, 2, 3, 4, 2, 1]
print(Solution([10, 40, 200, 1000, 60, 30]))

# Return [2, 1, 2, 3, 2, 2, 1]
print(Solution([4,1,4,6,5,3,1]))