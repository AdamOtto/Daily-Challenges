"""
Given an integer k and a string s, find the length of the longest
substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the
longest substring with k distinct characters is "bcb".
"""
def Solution(ar, k):
    if len(ar) <= k:
        return ar
    low = 0
    high = min(low + k, len(ar) - 1)
    highest = 0
    retVal = ""
    while high < len(ar):
        distChar = checkDistChar(ar[low:high])
        if distChar <= k:
            highest = max(highest, len(ar[low:high]))
            if highest > len(retVal):
                retVal = ar[low:high]
            high += 1
        else:
            low += 1
    return retVal

def checkDistChar(ar):
    d = set()
    for a in ar:
        d.add(a)
    return len(d)

# Return bcb
print(Solution("abcba", 2))

# Return elloworl
print(Solution("helloworld", 5))

# Return edcbaaaaa
print(Solution("abcdefgedcbaaaaaa", 5))