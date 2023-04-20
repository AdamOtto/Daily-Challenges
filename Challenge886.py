"""
The edit distance between two strings refers to the
minimum number of character insertions, deletions, and
substitutions required to change one string to the other.

For example, the edit distance between “kitten” and “sitting”
is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""
def Solution(s1, s2, i1, i2):
    if i1 == 0:
        return i2
    if i2 == 0:
        return i1
    
    if s1[i1 - 1] == s2[i2 - 1]:
        return Solution(s1, s2, i1 - 1, i2 - 1)
    
    return 1 + min(Solution(s1, s2, i1, i2 - 1), Solution(s1, s2, i1 - 1, i2), Solution(s1, s2, i1 - 1, i2 - 1))

# Return 3
print(Solution("kitten", "sitting", len("kitten"), len("sitting")))
# Return 4
print(Solution("asdfhello", "hello", len("asdfhello"), len("hello")))