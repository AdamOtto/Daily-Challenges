"""
Given a string s and a list of words words, where each word is the same length,
find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog"
and words = ["cat", "dog"], return [0, 13],
since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"],
return [] since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""
def Solution(s, words):
    wl = len(words)
    if wl == 0:
        return []
    wwl = len(words[0])
    sl = len(s)
    retVal = []

    for i in range(0, sl - (wl * wwl) + 1):
        addVal = True
        ss = s[i:i+(wl * wwl)]
        for j in words:
            if not ss.__contains__(j):
                addVal = False
                break
        if addVal:
            retVal.append(i)
    return retVal

# Return [0, 13]
print(Solution("dogcatcatcodecatdog", ["cat", "dog"]))

# Return []
print(Solution("barfoobazbitbyte", ["dog", "cat"]))

# Return [0, 10, 25, 35]
print(Solution("helloworldworldhellohellohelloworldworldhello", ["hello", "world"]))