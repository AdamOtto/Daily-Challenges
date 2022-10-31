"""
UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, corresponds to the three bytes
11100010 10000010 10101100. The rules for mapping characters are as follows:

 - For a single-byte character, the first bit must be zero.
 - For an n-byte character, the first byte starts with n ones and a zero.
   The other n - 1 bytes all start with 10.
   
Visually, this can be represented as follows.

 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Write a program that takes in an array of integers representing byte values, and returns whether it is a valid UTF-8 encoding.
"""
def Solution(ar):
    if len(ar) % 8 != 0:
        return False
    l = int(len(ar) / 8)
    
    if CheckFirstByte(ar, l):
        for i in range(8, l * 8, 8):
            if not checkRemainingBytes(ar[i: i + 8]):
                return False
    else:
        return False
    return True

def CheckFirstByte(ar, l):
    if l == 1:
        if ar[0] == 0:
            return True
        else:
            return False
    else:
        i = 0
        while i < l:
            if ar[i] != 1:
                return False
            i += 1
        if ar[i] != 0:
            return False
        return True

def checkRemainingBytes(byte):
    if byte[0] == 1 and byte[1] == 0:
        return True
    return False


# Return True
in1 = [0,1,0,1,0,1,0,0]
print(Solution(in1))

# Return False
in1 = [1,1,0,1,0,1,0,0]
print(Solution(in1))

# Return True
in1 = [1,1,1,0,0,1,0,0,  1,0,1,1,1,1,0,0,  1,0,0,1,0,0,0,0]
print(Solution(in1))

# Return False
in1 = [1,1,1,1,1,0,0,0,  1,0,1,1,1,1,0,0,  1,0,0,1,0,0,0,0,  1,0,1,1,1,1,0,1,  1,1,1,1,1,1,1,1,]
print(Solution(in1))

# Return True
in1 = [1,1,1,1,1,0,0,0,  1,0,1,1,1,1,0,0,  1,0,0,1,0,0,0,0,  1,0,1,1,1,1,0,1,  1,0,1,1,1,1,1,1,]
print(Solution(in1))