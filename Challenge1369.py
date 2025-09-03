"""
Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
"""
def Solution(ar):
    retVal = []
    l = len(ar)
    if l < 4:
        return False

    for i in range(0, l - 3):
        for j in range(1, l - 2):
            for k in range(2, l - 1):
                A = ar[0:i+1]
                B = ar[i+1:j+1]
                C = ar[j+1:k+1]
                D = ar[k+1:l]
                #print(A + "." + B + "." + C + "." + D)
                if IPCheck(A + "." + B + "." + C + "." + D):
                    retVal.append(A + "." + B + "." + C + "." + D)
    return retVal

def IPCheck(ar):
    val = ar.split(".")
    for s in val:
        if s == '':
            return False
        if len(s) > 1 and s[0] == "0":
            return False
        if int(s) < 0 or int(s) > 255:
            return False
    return True


# Return ['254.25.40.123', '254.254.0.123']
print(Solution("2542540123"))
# Return ['1.2.0.34', '1.20.3.4', '12.0.3.4']
print(Solution("12034"))
# Return ['0.113.104.54']
print(Solution("011310454"))