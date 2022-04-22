"""
The edit distance between two strings refers to the
minimum number of character insertions, deletions, and substitutions
required to change one string to the other.
For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”,
substitute the “e” for “i”,
and append a “g”.

Given two strings, compute the edit distance between them.
"""

def Solution(ar1, ar2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    
    if ar1[m - 1] == ar2[n - 1]:
        return Solution(ar1, ar2, m - 1, n - 1)
    return 1 + min(Solution(ar1, ar2, m - 1, n),
                   Solution(ar1, ar2, m, n - 1),
                   Solution(ar1, ar2, m - 1, n - 1))

# Return 1
print(Solution("cat", "rat", 3, 3))
# Return 3
print(Solution("kitten", "sitting", len("kitten"), len("sitting")))
# Return 4
print(Solution("always", "someways", len("always"), len("someways")))