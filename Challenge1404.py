"""
Given a string and a pattern, find the starting indices of all occurrences
of the pattern in the string. For example,
given the string "abracadabra" and the pattern "abr",
you should return [0, 7].
"""
def Solution(ar, pat):
    l = len(ar)
    lp = len(pat)
    patHash = hash(pat)
    retVal = []
    for i in range(lp, l):
        temp = hash(ar[i - lp: i])
        if temp == patHash:
            retVal.append(i - lp)
    return retVal

# Return [0, 7]
print(Solution("abracadabra", "abr"))
# Return [2]
print(Solution("HelloWorld", "ll"))
# Return [2,32]
print(Solution("Everyone likes me said Caul Shivers the most feared man in the North", "er"))