"""
You are given a hexadecimal-encoded string that has been XOR'd against a single char.

Decrypt the message. For example, given the string:

7a575e5e5d12455d405e561254405d5f1276535b5e4b12715d565b5c551262405d505e575f
You should be able to decrypt it and get:

Hello world from Daily Coding Problem

Note: Solution does not work.  The key may not be a printable char or my conversions are wrong.
Could not solve this in an hour.
"""
import string

def Solution(ar):
    for i in string.printable:
        retVal = "Decrypting with " + str(i) + ": "
        retVal += sxor(i,ar)
        print(retVal)
        print()
    return
    
def sxor(s1,s2):
    retVal = ""
    curKey = int(format(ord(s1), "x"), 16)
    for j in range(1, len(s2)):
            cur = int(s2[j-1:j+1], 16)
            retVal += chr(cur ^ curKey)
    return retVal

print(Solution("7a575e5e5d12455d405e561254405d5f1276535b5e4b12715d565b5c551262405d505e575f"))
