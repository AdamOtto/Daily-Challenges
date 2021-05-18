"""
Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""

def Solution(ar, key):
    l = len(ar)
    lk = len(key)
    retVal = []
    i = 0

    while i < l - lk:
        addValue = True
        if ar[i] == key[0]:
            temp = i + 1
            for j in range(1, lk):
                if ar[temp] != key[j]:
                    addValue = False
                    break
                temp += 1
            if addValue:
                retVal.append(i)
                i = temp
                continue
        i += 1
    return retVal

in1 = "abracadabra"
in2 = "abr"
print(Solution(in1, in2))