"""
Implement the function embolden(s, lst) which takes in a string s
and list of substrings lst, and wraps all substrings
in s with an HTML bold tag <b> and </b>.

If two bold tags overlap or are contiguous, they should be merged.

For example, given s = abcdefg and lst = ["bc", "ef"],
return the string a<b>bc</b>d<b>ef</b>g.

Given s = abcdefg and lst = ["bcd", "def"],
return the string a<b>bcdef</b>g, since they overlap.
"""

def embolden(s, lst):
    l = len(s)
    retVal = ""
    rng = [0] * l
    
    for ls in lst:
        ind = s.find(ls)
        for i in range(ind, ind + len(ls)):
            rng[i] = 1
    #print(s)
    #print(rng)
    One = False
    for i in range(l):
        if One and rng[i] == 0:
            retVal += "</b>"
            retVal += s[i]
            One = False
        elif not One and rng[i] == 1:
            retVal += "<b>"
            retVal += s[i]
            One = True
        else:
            retVal += s[i]
    
    if rng[l - 1] == 1:
        retVal += "</b>"
    return retVal

# Return a<b>bc</b>d<b>ef</b>g
print(embolden("abcdefg", ["bc", "ef"]))
# Return a<b>bcdef</b>g
print(embolden("abcdefg", ["bcd", "def"]))
# Return a<b>bcdefg</b>
print(embolden("abcdefg", ["bcd", "efg"]))