"""
Given an integer, find the next permutation of it in absolute order.
For example, given 48975, the next permutation would be 49578.

*Assume return False if next permutation doesn't exist.
"""
from itertools import permutations
import functools

def Solution(ar):
    res = list(map(int, str(ar)))
    t = list(permutations(res, len(res)))
    t = sorted(t)
    if t.index(tuple(res)) + 1 < len(t):
        return functools.reduce(lambda sub, ele: sub * 10 + ele, t[t.index(tuple(res)) + 1])
    return False

# Return 49578
print(Solution(48975))
# Return False
print(Solution(951))
# Return 1243
print(Solution(1234))