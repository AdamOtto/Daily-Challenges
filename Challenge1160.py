"""
You are given a string formed by concatenating several words corresponding
to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of
'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357.
"""
def dictEmpty(d):
    for (key, val) in d.items():
        if val >= 1:
            return True
    return False

def Solution(ar):
    d = {}
    retVal = ''
    for a in ar:
        if a.lower() in d:
            d[a.lower()] += 1
        else:
            d[a.lower()] = 1

    while dictEmpty(d):
        # Zero
        if 'z' in d and 'e' in d and 'r' in d and 'o' in d:
            if d['z'] >= 1 and d['e'] >= 1 and d['r'] >= 1 and d['o'] >= 1:
                d['z'] -= 1
                d['e'] -= 1
                d['r'] -= 1
                d['o'] -= 1
                retVal += '0'

        # One

        if 'o' in d and 'n' in d and 'e' in d:
            if d['o'] >= 1 and d['n'] >= 1 and d['e'] >= 1:
                d['o'] -= 1
                d['n'] -= 1
                d['e'] -= 1
                retVal += '1'

        # Two

        if 't' in d and 'w' in d and 'o' in d:
            if d['t'] >= 1 and d['w'] >= 1 and d['o'] >= 1:
                d['t'] -= 1
                d['w'] -= 1
                d['o'] -= 1
                retVal += '2'

        # Eight
        if 'e' in d and 'i' in d and 'g' in d and 'h' in d and 't' in d:
            if d['e'] >= 1 and d['i'] >= 1 and d['g'] >= 1 and d['h'] >= 1 and d['t'] >= 1:
                d['e'] -= 1
                d['i'] -= 1
                d['g'] -= 1
                d['h'] -= 1
                d['t'] -= 1
                retVal += '8'

        # Four
        if 'f' in d and 'o' in d and 'u' in d and 'r' in d:
            if d['f'] >= 1 and d['o'] >= 1 and d['u'] >= 1 and d['r'] >= 1:
                d['f'] -= 1
                d['o'] -= 1
                d['u'] -= 1
                d['r'] -= 1
                retVal += '4'

        # Five
        if 'f' in d and 'i' in d and 'v' in d and 'e' in d:
            if d['f'] >= 1 and d['i'] >= 1 and d['v'] >= 1 and d['e'] >= 1:
                d['f'] -= 1
                d['i'] -= 1
                d['v'] -= 1
                d['e'] -= 1
                retVal += '5'

        # Six
        if 's' in d and 'i' in d and 'x' in d:
            if d['s'] >= 1 and d['i'] >= 1 and d['x'] >= 1:
                d['s'] -= 1
                d['i'] -= 1
                d['x'] -= 1
                retVal += '6'

        # Three
        if 't' in d and 'h' in d and 'r' in d and 'e' in d:
            if d['t'] >= 1 and d['h'] >= 1 and d['r'] >= 1 and d['e'] >= 2:
                d['t'] -= 1
                d['h'] -= 1
                d['r'] -= 1
                d['e'] -= 2
                retVal += '3'

        # Seven
        if 's' in d and 'e' in d and 'v' in d and 'n' in d:
            if d['s'] >= 1 and d['e'] >= 2 and d['v'] >= 1 and d['n'] >= 1:
                d['s'] -= 1
                d['e'] -= 2
                d['v'] -= 1
                d['n'] -= 1
                retVal += '7'

        # Nine
        if 'n' in d and 'i' in d and 'e' in d:
            if d['n'] >= 2 and d['i'] >= 1 and d['e'] >= 1:
                d['n'] -= 2
                d['i'] -= 1
                d['e'] -= 1
                retVal += '9'

    return ''.join(sorted(retVal))


# Return 357
print(Solution('niEsevehrtfeev'))

# Return 0112359
print(Solution('otnoneoneneoweriheveiezrft'))

# Return 0124689
print(Solution('zeroonetwofoursixeightnine'))