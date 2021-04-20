"""
Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"]
"""

def Solution(in1):
    l = len(in1)
    retVal = []
    d = {}
    for i in reversed(range(0, l)):
        if in1[i] not in d:
            d[in1[i]] = []
        d[in1[i]].append(i)

    i = 0
    while i < l:
        noPalidromeFound = True
        for index in d[in1[i]]:
            if i != index and isPalindrome(in1, i, index):
                retVal.append(in1[i:index+1])
                noPalidromeFound = False
                i = index
                break
        if noPalidromeFound:
            retVal.append(in1[i])
        i += 1
    return retVal

def isPalindrome(in1, i, j):
    if i >= j:
        return False
    while i < j:
        if in1[i] == in1[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

#in1 = "racecarannakayak"
#in1 = "abc"
in1 = "acaacatestsetestset"
print(Solution(in1))