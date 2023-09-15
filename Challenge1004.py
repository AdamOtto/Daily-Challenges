"""
Given a list of numbers L, implement a method sum(i, j) which
returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5],
sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
"""
def Sum(i, j):
    return sum(L[i:j])
L = [1, 2, 3, 4, 5]
print(Sum(1,3))