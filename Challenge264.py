"""
Given a set of characters C and an integer k,
a De Bruijn sequence is a cyclic sequence in which every possible k-length
string of characters in C occurs exactly once.

For example, suppose C = {0, 1} and k = 3.
Then our sequence should contain the substrings
{'000', '001', '010', '011', '100', '101', '110', '111'}
and one possible solution would be 00010111.

Create an algorithm that finds a De Bruijn sequence.
"""

def findSubStrings(C, k):
    retVal = []
    subStr = [C[0]] * k
    tempStr = ""
    retVal.append(tempStr.join(subStr))
    for i in range( pow(len(C), k) - 1):
        AddToSubStr(0, subStr, C)
        tempStr = ""
        retVal.append(tempStr.join(subStr))
    #print(retVal)
    return retVal

def AddToSubStr(cur, subStr, C):
    if cur >= len(subStr):
        return
    t = C.index(subStr[cur])
    if t == len(C) - 1:
        subStr[cur] = C[0]
        AddToSubStr(cur + 1, subStr, C)
    else:
        subStr[cur] = C[t + 1]
    return

def CheckBruijnSequence(subStr, Seq):

    for s in subStr:
        if Seq.find(s) == -1 and Seq.find(s[::-1]) == -1:
            return False
    return True

def BruteForceSolution(SubStr, C):
    retVal = [C[0]]
    temp = ""
    temp = temp.join(retVal)
    while not CheckBruijnSequence(SubStr, temp):
        BruteForceSolutionHelper(0, retVal, C)
        temp = ""
        temp = temp.join(retVal)
    return temp

def BruteForceSolutionHelper(cur, subStr, C):
    if cur >= len(subStr):
        subStr.append(C[0])
        return
    t = C.index(subStr[cur])
    if t == len(C) - 1:
        subStr[cur] = C[0]
        BruteForceSolutionHelper(cur + 1, subStr, C)
    else:
        subStr[cur] = C[t + 1]
    return

C = ["0", "1"]
k = 3
subStr = findSubStrings(C, k)
#print(findSubStrings(C, k))
print(BruteForceSolution(subStr, C))


C = ["a", "b", "c"]
k = 2
subStr = findSubStrings(C, k)
#print(findSubStrings(C, k))
print(BruteForceSolution(subStr, C))


C = ["w", "x", "y", "z"]
k = 2
subStr = findSubStrings(C, k)
#print(findSubStrings(C, k))
print(BruteForceSolution(subStr, C))