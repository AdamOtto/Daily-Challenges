"""
Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses
subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.
"""
def RomanConvert(l):
    if l == 'M':
        return 1000
    elif l == 'D':
        return 500
    elif l == 'C':
        return 100
    elif l == 'L':
        return 50
    elif l == 'X':
        return 10
    elif l == 'V':
        return 5
    elif l == 'I':
        return 1

def RomanTier(l):
    if l == 'M':
        return 10
    elif l == 'D':
        return 8
    elif l == 'C':
        return 7
    elif l == 'L':
        return 5
    elif l == 'X':
        return 4
    elif l == 'V':
        return 2
    elif l == 'I':
        return 1

def Solution(ar):
    l = len(ar)
    i = l - 1
    retVal = 0
    while i >= 0:
        if i == 0:
            retVal += RomanConvert(ar[i])
        elif RomanConvert(ar[i - 1]) < RomanConvert(ar[i]):
            if RomanTier(ar[i - 1]) == RomanTier(ar[i]) - 1:
                retVal += RomanConvert(ar[i]) - RomanConvert(ar[i - 1])
                i -= 1
            else:
                return False
        else:
            retVal += RomanConvert(ar[i])
        i -= 1
    return retVal

#Return 4
print(Solution("IV"))

#Return 44
print(Solution("XLIV"))

#Return 444
print(Solution("CDXLIV"))

#Return 4444
print(Solution("MMMMCDXLIV"))