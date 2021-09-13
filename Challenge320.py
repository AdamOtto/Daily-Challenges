"""
Given a string, find the length of the smallest window that contains every distinct character.
Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
"""

# O(n)
def Solution(ar):
    l = len(ar)
    if l <= 1:
        return l
    
    sets = set()
    sets.add(ar[0])
    retVal = 0
    curCount = 1
    for i in range(1, l):
        if ar[i] not in sets:
            sets.add(ar[i])
            curCount += 1
        else:
            retVal = max(retVal, curCount)
            if ar[i - 1] == ar[i]:
                curCount = 1
    return max(retVal, curCount)

# Return 5
print(Solution("jiujitsu"))
# Return 1
print(Solution("a"))
# Return 3
print(Solution("abc"))
# Return 4
print(Solution("abcabcddefg"))
# Return 3
print(Solution("abbccded"))