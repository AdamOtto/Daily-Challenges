"""
A permutation can be specified by an array P,
where P[i] represents the location of the element at i in
the permutation. For example, [2, 1, 0] represents the permutation
where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array.
For example, given the array
["a", "b", "c"]
and the permutation
[2, 1, 0]
return ["c", "b", "a"].
"""

def Solution(ar, P):
    l = len(ar)
    retVal = [None] * l
    for i in range(l):
        retVal[i] = ar[P[i]]
    return retVal

#Return ['c', 'b', 'a']
print(Solution(["a", "b", "c"], [2, 1, 0]))

#Return [10, 0, 1, 3, 6, 4, 9, 2, 8, 5, 7]
print(Solution([0,1,2,3,4,5,6,7,8,9,10], [10,0,1,3,6,4,9,2,8,5,7]))