"""
Soundex is an algorithm used to categorize phonetically,
such that two names that sound alike but are spelled differently have the same representation.

Soundex maps every name to a string consisting of
one letter and three numbers, like M460.

One version of the algorithm is as follows:
    - Remove consecutive consonants with the same sound (for example, change ck -> c).
    - Keep the first letter. The remaining steps only apply to the rest of the string.
    - Remove all vowels, including y, w, and h.
    - Replace all consonants with the following digits:
        b, f, p, v → 1
        c, g, j, k, q, s, x, z → 2
        d, t → 3
        l → 4
        m, n → 5
        r → 6
        
    - If you don't have three numbers yet, append zeros until you do. Keep the first three numbers.

Using this scheme, Jackson and Jaxen both map to J250.
Implement Soundex.
"""
from itertools import permutations

def RemoveConsecutiveConsonants(ar):
    if len(ar) < 2:
        return ar
    
    allPerm = permutations("bfpv", 2)
    for a in allPerm:
        if a is not None:
            ar = ar.replace(list2Str(a), a[0])
    ar = ar.replace("ff", "f")
    ar = ar.replace("pp", "p")
    ar = ar.replace("bb", "b")
    ar = ar.replace("vv", "v")
    
    allPerm = permutations("cgjkqsxz", 2)
    for a in allPerm:
        if a is not None:
            ar = ar.replace(list2Str(a), a[0])
    ar = ar.replace("ss", "s")
    ar = ar.replace("gg", "g")
    ar = ar.replace("jj", "j")
    ar = ar.replace("kk", "k")
    ar = ar.replace("qq", "q")
    ar = ar.replace("ss", "s")
    ar = ar.replace("xx", "x")
    ar = ar.replace("zz", "z")
    
    ar = ar.replace("dt", "d")
    ar = ar.replace("td", "t")
    ar = ar.replace("tt", "t")
    ar = ar.replace("dd", "d")
    
    ar = ar.replace("ll", "l")
    
    ar = ar.replace("mm", "m")
    ar = ar.replace("nn", "n")
    ar = ar.replace("nm", "n")
    ar = ar.replace("mn", "m")
    
    ar = ar.replace("rr", "r")
    
    return ar
    
def RemoveVowels(ar):
    ar = ar.replace("a", "")
    ar = ar.replace("e", "")
    ar = ar.replace("i", "")
    ar = ar.replace("o", "")
    ar = ar.replace("u", "")
    ar = ar.replace("y", "")
    ar = ar.replace("w", "")
    ar = ar.replace("h", "")
    return ar

def ReplaceConsonants(ar):
    #1
    ar = ar.replace("b", "1")
    ar = ar.replace("f", "1")
    ar = ar.replace("p", "1")
    ar = ar.replace("v", "1")
    
    #2
    ar = ar.replace("c", "2")
    ar = ar.replace("g", "2")
    ar = ar.replace("j", "2")
    ar = ar.replace("k", "2")
    ar = ar.replace("q", "2")
    ar = ar.replace("s", "2")
    ar = ar.replace("x", "2")
    ar = ar.replace("z", "2")
    
    #3
    ar = ar.replace("d", "3")
    ar = ar.replace("t", "3")
    
    #4
    ar = ar.replace("l", "4")

    #5
    ar = ar.replace("m", "5")
    ar = ar.replace("n", "5")
    
    #6
    ar = ar.replace("r", "6")
    
    return ar

def CountNum(ar):
    count = 0
    for c in ar:
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            count += 1
    return count

def RemoveNumbers(ar):
    copy = list(ar)
    while CountNum(list2Str(copy)) > 3:
        for i in reversed(range(0, len(copy))):
            if ord(copy[i]) >= ord('0') and ord(copy[i]) <= ord('9'):
                copy.pop(i)
                break
    return list2Str(copy)

def list2Str(ar):
    retVal = ""
    return retVal.join(ar)

def Solution(ar):
    first = ar[0].upper()
    rest = ar[1:].lower()
    rest = RemoveConsecutiveConsonants(rest)
    rest = RemoveVowels(rest)
    rest = ReplaceConsonants(rest)
    if CountNum(rest) < 3:
        while CountNum(rest) < 3:
            rest += '0'
    elif CountNum(rest) >= 4:
        rest = RemoveNumbers(rest)
    return first + rest


# Return J250
print(Solution("Jackson"))
# Return J250
print(Solution("Jaxen"))
# Return E251
print(Solution("example"))
# Return E251
print(Solution("ekzampul"))
# Return A234
print(Solution("actually"))
# Return A224
print(Solution("ackchoolee"))