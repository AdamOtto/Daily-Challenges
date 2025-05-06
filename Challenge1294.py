"""
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""
def encoding(ar):
    l = len(ar)
    count = 0
    val = ar[0]
    retVal = ""
    for i in range(l):
        if ar[i] == val:
            count += 1
        else:
            retVal += str(count) + str(val)
            count = 1
            val = ar[i]
    retVal += str(count) + str(val)
    return retVal
        
def decoding(ar):
    l = len(ar)
    if l % 2 > 0:
        return False
    count = 0
    val = None
    retVal = ""
    for i in range(1,l,2):
        count = int(ar[i - 1])
        val = ar[i]
        retVal += "".join([val] * count)
    return retVal

# Return 4A3B2C1D2A and AAAABBBCCDAA
print(encoding("AAAABBBCCDAA"))
print(decoding("4A3B2C1D2A"))
# Return 1122334455 and 122333444455555
print(encoding("122333444455555"))
print(decoding("1122334455"))
#
print(encoding("EveryoneLikesMeSaidCaulShiversTheMostFearedManInTheNorth"))
print(decoding("1E1v1e1r1y1o1n1e1L1i1k1e1s1M1e1S1a1i1d1C1a1u1l1S1h1i1v1e1r1s1T1h1e1M1o1s1t1F1e1a1r1e1d1M1a1n1I1n1T1h1e1N1o1r1t1h"))