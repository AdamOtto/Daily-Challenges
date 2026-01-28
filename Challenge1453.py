"""
A permutation can be specified by an array P, where P[i] represents
the location of the element at i in the permutation.
For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array.
For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
"""

def Solution(ar, per):
    l = len(ar)
    retVal = []
    for p in per:
        if p < l:
            retVal.append(ar[p])
        else:
            return False
    return retVal

# Return ['c', 'b', 'a']
print(Solution(["a", "b", "c"], [2, 1, 0]))

# Return ['e', 'a', 'c', 'b', 'd']
print(Solution(["a", "b", "c", "d", "e"], [4, 0, 2, 1, 3]))