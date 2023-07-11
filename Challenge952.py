"""
You are given a string formed by concatenating several words corresponding
to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram
of 'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order.
In the example above, this would be 357.
"""
def Solution(ar):
    d = {}
    initD(d)
    for a in ar.lower():
        if a not in d:
            return None
        d[a] += 1
    retVal = ""
    if d['z'] >= 1 and d['e'] >= 1 and d['r'] >= 1 and d['o'] >= 1:
        d['z'] -= 1
        d['e'] -= 1
        d['r'] -= 1
        d['o'] -= 1
        retVal += "0"
    if d['e'] >= 1 and d['i'] >= 1 and d['g'] >= 1 and d['h'] >= 1 and d['t'] >= 1:
        d['e'] -= 1
        d['i'] -= 1
        d['g'] -= 1
        d['h'] -= 1
        d['t'] -= 1
        retVal += "8"
    if d['s'] >= 1 and d['e'] >= 2 and d['v'] >= 1 and d['n'] >= 1:
        d['s'] -= 1
        d['e'] -= 2
        d['v'] -= 1
        d['n'] -= 1
        retVal += "7"
    if d['o'] >= 1 and d['n'] >= 1 and d['e'] >= 1:
        d['o'] -= 1
        d['n'] -= 1
        d['e'] -= 1
        retVal += "1"
    if d['t'] >= 1 and d['w'] >= 1 and d['o'] >= 1:
        d['t'] -= 1
        d['w'] -= 1
        d['o'] -= 1
        retVal += "2"
    if d['t'] >= 1 and d['h'] >= 1 and d['r'] >= 1 and d['e'] >= 2:
        d['t'] -= 1
        d['h'] -= 1
        d['r'] -= 1
        d['e'] -= 2
        retVal += "3"
    if d['f'] >= 1 and d['o'] >= 1 and d['u'] >= 1 and d['r'] >= 1:
        d['f'] -= 1
        d['o'] -= 1
        d['u'] -= 1
        d['r'] -= 1
        retVal += "4"
    if d['f'] >= 1 and d['i'] >= 1 and d['v'] >= 1 and d['e'] >= 1:
        d['f'] -= 1
        d['i'] -= 1
        d['v'] -= 1
        d['e'] -= 1
        retVal += "5"
    if d['s'] >= 1 and d['i'] >= 1 and d['x'] >= 1:
        d['s'] -= 1
        d['i'] -= 1
        d['x'] -= 1
        retVal += "6"
    if d['n'] >= 2 and d['i'] >= 1 and d['e'] >= 1:
        d['n'] -= 2
        d['i'] -= 1
        d['e'] -= 1
        retVal += "9"
    return "".join(sorted(retVal))

def initD(d):
    for a in "zero":
        if a not in d:
            d[a] = 0
    for a in "one":
        if a not in d:
            d[a] = 0
    for a in "two":
        if a not in d:
            d[a] = 0
    for a in "three":
        if a not in d:
            d[a] = 0
    for a in "four":
        if a not in d:
            d[a] = 0
    for a in "five":
        if a not in d:
            d[a] = 0
    for a in "six":
        if a not in d:
            d[a] = 0
    for a in "seven":
        if a not in d:
            d[a] = 0
    for a in "eight":
        if a not in d:
            d[a] = 0
    for a in "nine":
        if a not in d:
            d[a] = 0

    
# Return 357
print(Solution('niesevehrtfeev'))

# Return 0124689
print(Solution('zeroonetwofoursixeightnine'))

# Return 123
print(Solution('woenetrothe'))