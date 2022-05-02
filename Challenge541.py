"""
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive
characters as a single count and character.
For example, the string "AAAABBBCCDAA"
would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of
alphabetic characters. You can assume the string to be decoded is valid.
"""

def SolutionEncode(ar):
    retVal = ""
    last = ar[0]
    count = 1
    for i in range(1, len(ar)):
        if ar[i] != ar[i-1]:
            retVal += str(count)
            retVal += str(last)
            last = ar[i]
            count = 1
        else:
            count += 1
    retVal += str(count)
    retVal += str(last)
    return retVal

def SolutionDecode(ar):
    num = ""
    retVal = ""
    for i in range(0, len(ar)):
        if ord(ar[i]) >= ord('0') and  ord(ar[i]) <= ord('9'):
            num += ar[i]
        else:
            for j in range(int(num)):
                retVal += ar[i]
            num = ""
    return retVal

# Return 4A3B2C1D2A and AAAABBBCCDAA
t1 = SolutionEncode("AAAABBBCCDAA")
print(t1)
print(SolutionDecode(t1))

# Return 1h1e2l1o1w1o1r1l1d and helloworld
t1 = SolutionEncode("helloworld")
print(t1)
print(SolutionDecode(t1))