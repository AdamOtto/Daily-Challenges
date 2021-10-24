"""
You are given a string formed by concatenating several words
corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'.
Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order.
In the example above, this would be 357.
"""

def Solution(ar):
    ar = ar.lower()
    d = {}
    
    for i in range(ord('a'), ord('z') + 1):
        d[chr(i)] = 0
    
    retVal = ""
    for i in range(len(ar)):
            d[ar[i]] += 1
    count = len(ar)
    while count > 0:
        # zero
        if d['z'] >= 1 and d['e'] >= 1 and d['r'] >= 1 and d['o'] >= 1:
            retVal += "0"
            d['z'] -= 1
            d['e'] -= 1
            d['r'] -= 1
            d['o'] -= 1
            count -= 4
        # one
        if d['o'] >= 1 and d['n'] >= 1 and d['e'] >= 1:
            retVal += "1"
            d['o'] -= 1
            d['n'] -= 1
            d['e'] -= 1
            count -= 3
        # two
        if d['t'] >= 1 and d['w'] >= 1 and d['o'] >= 1:
            retVal += "2"
            d['t'] -= 1
            d['w'] -= 1
            d['o'] -= 1
            count -= 3
        # three
        if d['t'] >= 1 and d['h'] >= 1 and d['r'] >= 1 and d['e'] >= 2:
            retVal += "3"
            d['t'] -= 1
            d['h'] -= 1
            d['r'] -= 1
            d['e'] -= 2
            count -= 5
        # four
        if d['f'] >= 1 and d['o'] >= 1 and d['u'] >= 1 and d['r'] >= 1:
            retVal += "4"
            d['f'] -= 1
            d['o'] -= 1
            d['u'] -= 1
            d['r'] -= 1
            count -= 4
        # five
        if d['f'] >= 1 and d['i'] >= 1 and d['v'] >= 1 and d['e'] >= 1:
            retVal += "5"
            d['f'] -= 1
            d['i'] -= 1
            d['v'] -= 1
            d['e'] -= 1
            count -= 4
        # six
        if d['s'] >= 1 and d['i'] >= 1 and d['x'] >= 1:
            retVal += "6"
            d['s'] -= 1
            d['i'] -= 1
            d['x'] -= 1
            count -= 3
        # seven
        if d['s'] >= 1 and d['e'] >= 2 and d['v'] >= 1 and d['n'] >= 1:
            retVal += "7"
            d['s'] -= 1
            d['e'] -= 2
            d['v'] -= 1
            d['n'] -= 1
            count -= 5
        # eight
        if d['e'] >= 1 and d['i'] >= 2 and d['g'] >= 1 and d['h'] >= 1 and d['t'] >= 1:
            retVal += "8"
            d['e'] -= 1
            d['i'] -= 1
            d['g'] -= 1
            d['h'] -= 1
            d['t'] -= 1
            count -= 5
        # nine
        if d['n'] >= 2 and d['i'] >= 1 and d['e'] >= 1:
            retVal += "9"
            d['n'] -= 2
            d['i'] -= 1
            d['e'] -= 1
            count -= 4
    retVal = sorted(retVal)
    retVal = "".join(retVal)
    return retVal

# Return 357
in1 = 'niesevehrtfeev'
print(Solution(in1))

# Return 011111111223344556789 (one to fifteen)
in1 = 'onetwothreefourfivesixseveneightnineonezerooneoneonetwoonethreeonefouronefive'
in1 = sorted(in1)
in1 = "".join(in1)
print(Solution(in1))