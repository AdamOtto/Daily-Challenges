"""
Given a string with repeated characters, rearrange the
string so that no two adjacent characters are the same.
If this is not possible, return None.

For example, given "aaabbc", you could return "ababac".
Given "aaab", return None.
"""
def Solution(ar):
    if Checker(ar):
        return ar

    d = {}
    Uniqueletters = []

    for i in range(0, len(ar)):
        if ar[i] not in d:
            d[ar[i]] = 1
        else:
            d[ar[i]] += 1
        if ar[i] not in Uniqueletters:
            Uniqueletters.append(ar[i])

    retVal = Helper("", d, Uniqueletters)
    return retVal

def Helper(retVal, d, ul):
    empty = True
    for key, val in d.items():
        if val > 0:
            empty = False
            break
    if empty:
        if Checker(retVal):
            return retVal
        else:
            return None

    for l in ul:
        if d[l] >= 1:
            d[l] -= 1
            temp = retVal + l
            if Checker(temp):
                t = Helper(temp, d, ul)
                if t is not None:
                    return t
                else:
                    d[l] += 1
            else:
                d[l] += 1

def Checker(ar):
    l = len(ar)
    if l == 1:
        return True
    if l == 2:
        if ar[0] != ar[1]:
            return True
        else:
            return False
    for i in range(1, l - 1):
        if ar[i - 1] == ar[i] or ar[i] == ar[i + 1]:
            return False
    return True

# Return ababac
in1 = "aaabbc"
print(Solution(in1))

# Return None
in1 = "aaab"
print(Solution(in1))

# Return anan1n1212b242l2l2l2ljljkjkjkjkjsjsjsjsfsfsf9f8f3f3g3gdgdgeghg
in1 = "an1n1n2b14ljksf983jksljf23232222asdlfjkefsljfgjggjggjshglkjsdf"
print(Solution(in1))