"""
Given a string, return the first recurring character
in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b".
Given the string "abcdef", return null.
"""
def Solution(ar):
    d = set()
    l = len(ar)
    for i in range(l):
        if ar[i] in d:
            return ar[i]
        else:
            d.add(ar[i])
    return None

# Return b
print(Solution("acbbac"))
# Return None
print(Solution("abcdefg"))