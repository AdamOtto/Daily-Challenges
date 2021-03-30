"""
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

def Solution(in1):
    d = {}
    for s in in1:
        if s in d:
            return s
        else:
            d[s] = 1
    return None

in1 = "acbbac"
print(Solution(in1))