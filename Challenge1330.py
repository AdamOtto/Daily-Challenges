"""
Spreadsheets often use this alphabetical
encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id.
For example, given 1, return "A". Given 27, return "AA".
"""
def Solution(ar):
    cur = 26
    if ar < cur:
        return intToChar(ar)
    retVal = ""
    while cur < ar:
        retVal = intToChar(ar % cur) + retVal
        ar = ar // cur
    retVal = intToChar(ar) + retVal
    return retVal

def intToChar(ar):
    if 0 < ar and ar <= 26:
        return chr(ord('@') + ar)
    return ""

# Return AA
print(Solution(27))

# Return ALV
print(Solution(1010))

# Return PIKACHU
print(Solution(5054631369))