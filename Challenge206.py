"""
A permutation can be specified by an array P, where P[i]
represents the location of the element at i in the permutation.
For example, [2, 1, 0] represents the permutation where elements
at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array.
For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
"""

def Solution(toSwap, swapLoc):
    if len(toSwap) != len(swapLoc):
        return False
    l = len(toSwap)
    retVal = [0] * l
    for i in range(0, l):
        retVal[swapLoc[i]] = toSwap[i]
    return retVal

#in1 = ["a", "b", "c"]
#in2 = [2, 1, 0]
in1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
in2 = [7,1,5,4,3,2,6,0]
print(Solution(in1, in2))