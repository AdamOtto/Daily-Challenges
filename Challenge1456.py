"""
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

def Solution(ar):
    d = {}
    for a in ar:
        if a not in d:
            d[a] = 1
        else:
            return a
    return None


print(Solution("acbbac"))