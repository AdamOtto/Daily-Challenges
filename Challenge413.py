"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X?

For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

Notes:
The above example should have this solution: 3 unique ways
1, 1, 1, 1
3, 1
1, 3
"""

# O(n^2)
def Solution(N, ar):
    ar = sorted(ar)
    found = set()
    unique = []
    Helper(N, ar, [], unique)
    return len(unique), unique

def Helper(N, ar, cur, unique):
    if sum(cur) == N:
        if cur not in unique:
            unique.append(cur)
    
    for i in range(0, len(ar)):
        if ar[i] + sum(cur) <= N:
            t = cur.copy()
            t.append(ar[i])
            Helper(N, ar, t, unique)
    return

# Return (3, [[1, 1, 1, 1], [1, 3], [3, 1]])
N = 4
ar = [1, 3, 5]
print(Solution(N, ar))

# Return (5, [[1, 1, 1, 1, 1], [1, 1, 3], [1, 3, 1], [3, 1, 1], [5]])
N = 5
ar = [1, 3, 5]
print(Solution(N, ar))

# Return (31, ...)
N = 7
ar = [1, 2, 4]
print(Solution(N, ar))