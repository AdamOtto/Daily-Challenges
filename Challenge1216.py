"""
You are given an N by M 2D matrix of lowercase letters.
Determine the minimum number of columns that can be removed to
ensure that each row is ordered from top to bottom lexicographically.
That is, the letter at each column is lexicographically later as you go down each row.

It does not matter whether each row itself is ordered lexicographically.
"""
def Solution(ar):
    if len(ar) == 1:
        return 0
    retVal = 0
    for i in range(len(ar[0])):
        if len(ar[i]) > 1 and Helper(ar, i):
            retVal += 1
    return retVal
    
def Helper(ar, col):
    for i in range(1, len(ar)):
        if ord(ar[i][col]) < ord(ar[0][col]):
            return True
    return False
    
# Return 1
in1 = [['c', 'b', 'a'],
['d', 'a', 'f'],
['g', 'h', 'i']]
print(Solution(in1))

# Return 0
in1 = [['a', 'b', 'c', 'd', 'e', 'f', 'g']]
print(Solution(in1))

# Return 3
in1 = [['z', 'y', 'x'],
['w', 'v', 'u'],
['t', 's', 'r']]
print(Solution(in1))