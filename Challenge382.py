"""
Yesterday you implemented a function that encodes a hexadecimal string into Base64.

Write a function to decode a Base64 string back to a hexadecimal string.
"""

def Solution(ar):
    bits = ""
    for a in ar:
        if a != '=':
            bits += Base64toBit(a)
    while len(bits) % 8 != 0:
        bits += "0"
    i = 8
    retVal = ""
    while i < len(bits):
        retVal += chr(int(bits[i - 8:i], 2))
        i += 8
    retVal += chr(int(bits[i - 8:i], 2))
    return retVal

def Base64toBit(ar):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    retVal = "".join(bin(base64.index(ar))).replace("0b", "")
    while len(retVal) < 6:
        retVal = "0" + retVal
    return retVal

# Return 'Test'
print(Solution("VGVzdA=="))

# Return 'HelloWorld'
print(Solution("SGVsbG9Xb3JsZA=="))