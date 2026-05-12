"""
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""
def Solution(ar):
    s = set()
    for a in ar:
        if a not in s:
            s.add(a)
        else:
            return a
    return None

# Return b
print(Solution("acbbac"))

# Return None
print(Solution("abcdef"))