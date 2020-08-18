'''
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.

For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
'''

def SolEncode(in1):
    count = 1
    cur = in1[0]
    RetVal = ""
    for i in range(1,len(in1)):
        if cur == in1[i]:
            count += 1
        else:
            RetVal += str(count) + cur
            cur = in1[i]
            count = 1
    RetVal += str(count) + cur        
    #print(RetVal)
    return RetVal

def SolDecode(in1):
    RetVal = ""
    i = 0
    last = 0
    while i < len(in1):
        if isNumeric(in1[i]):
            i += 1
        else:
            t = int(in1[last:i])
            last = i + 1
            for j in range(0, t):
                RetVal += in1[i]
            i += 1
    return RetVal

def isNumeric(char):
    if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
        return True
    else:
        return False

#in1 = "AAAABBBCCDAA"
in1 = "ABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDE"
print("Input: " + in1)
t1 = SolEncode(in1)
print("Input encoded: " + t1)
t2 = SolDecode(t1)
print("Input decoded: " + t2)
if in1 == t2:
    print("Encoding and decoding works")
else:
    print("Error in encoding and decoding")