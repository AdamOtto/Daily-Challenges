"""
Spreadsheets often use this alphabetical encoding for its columns:
"A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id.
For example, given 1, return "A". Given 27, return "AA".
"""
def Solution(col):
    if col <= 0:
        return False
    retVal = ""
    while col > 0:
        if col % 26 == 0:
            retVal += "Z"
            col = int((col/26) - 1)
        else:
            retVal += intToChar(col % 26)
            col = int(col/26)
    return retVal[::-1]

def intToChar(num):
    temp = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    return temp[num - 1]


# Return A
print(Solution(1))
# Return AA
print(Solution(27))
# Return PIKACHU
print(Solution(5054631369))