"""
Read this Wikipedia article on Base64 encoding.

Implement a function that converts a hex string to base64.
"""

def Solution(ar):
    binary = ""
    
    for a in ar:
        binary += string2bin(a)
    l = len(binary)
    i = 0
    retVal = ""
    while i < l:
        i = min(i, l)
        retVal += Base64Table(binary[i:i+6])
        i += 6
    padding = len(ar) % 3
    if padding != 0:
        for i in range(3 - padding):
            retVal += "="
    return retVal

def Base64Table(ar):
    if len(ar) < 6:
        while len(ar) < 6:
            ar += "0"
    i = int(ar, 2)
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return base64[i]

def string2bin(string):
    return ''.join(bin(ord(c)) for c in string).replace('b','')


print(Solution("Test"))