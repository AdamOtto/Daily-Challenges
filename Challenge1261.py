"""
Given a list of words, find all pairs of unique indices such that
the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"],
return [(0, 1), (1, 0), (2, 3)].
"""

def Solution(ar):
    retVal = []
    for i in range(len(ar)):
        l = len(ar)
        for j in range(0, len(ar)):
            if i != j and isPalindrom(ar[i], ar[j]):
                retVal.append( (i, j) )
    return retVal

def isPalindrom(in1, in2):
    in3 = in1 + in2
    in3Palin = True
    low = 0
    high = len(in3) - 1
    while low <= high:
        if in3[low] != in3[high]:
            in3Palin = False
            break
        low += 1
        high -= 1
    return in3Palin

# Return [(0, 1), (1, 0), (2, 3)]
print(Solution(["code", "edoc", "da", "d"]))

# Return [(0, 5), (0, 7), (1, 5), (1, 6), (1, 7), (2, 1), (2, 4), (4, 0), (4, 3), (5, 0), (6, 7), (7, 1), (7, 2)]
print(Solution(["abc", "ab", "b", "c", "cb", "cba", "a", "ba"]))