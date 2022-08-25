"""
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

def Solution(ar):
    for i in range(1, len(ar)):
        if ar[i - 1] == ar[i]:
            return ar[i]
    return None
# Return b
print(Solution("acbbac"))

# Return None
print(Solution("abcdef"))