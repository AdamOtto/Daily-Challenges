"""
Given an array of positive integers,
divide the array into two subsets such that the difference between
the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets
{10, 25} and {5, 15, 20}, which has a difference of 5,
which is the smallest possible difference.
"""
# O(nlog(n))
def Solution(in1):

    sortedIn1 = list(reversed(sorted(in1)))
    #print(t)
    retVal1 = []
    retVal2 = []
    retVal2.append(sortedIn1.pop(0))

    while len(sortedIn1) != 0:
        t = sortedIn1.pop(0)
        if sum(retVal1) < sum(retVal2):
            retVal1.append(t)
        elif sum(retVal1) >= sum(retVal2):
            retVal2.append(t)

    print("Difference of sets: " + str(abs(sum(retVal1) - sum(retVal2))))
    print(retVal1)
    print(retVal2)


#in1 = [5, 10, 15, 20, 25]
in1 = [15,150,25,35,35,40,45]
Solution(in1)