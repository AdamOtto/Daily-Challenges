"""
Given a set of distinct positive integers, find the largest subset such
that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20].
Given [1, 3, 6, 24], return [1, 3, 6, 24].
"""
# O(n^2)
def Solution(ar):
    l = len(ar)
    subs = []

    subs.append( [ ar[l - 1] ])

    for i in reversed(range(0, l - 1)):
        makeNewSubs = True
        for j in range(0, len(subs)):
            if checkIfDivisible(subs[j], ar[i]):
                subs[j].append(ar[i])
                makeNewSubs = False

        if makeNewSubs:
            subs.append( [ar[i]] )
    print(subs)
    retVal = subs[0]
    for i in range(1, len(subs)):
        if len(subs[i]) > len(retVal):
            retVal = subs[i]
    return retVal


def checkIfDivisible(ar, div):
    for i in range(0, len(ar)):
        if not DivCheck(ar[i], div):
            return False
    return True

def DivCheck(a, b):
    return a % b == 0 or b % a == 0

# in1 = [3, 5, 10, 20, 21]
# in1 =[1, 3, 6, 24]
in1 = [2,3,5,14,50,75,56,23,34,25,26,27,80,100,101,120, 125, 150, 300]
in1.sort()
print(Solution(in1))
