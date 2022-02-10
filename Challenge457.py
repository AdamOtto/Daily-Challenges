"""
Given a word W and a string S, find all
starting indices in S which are anagrams of W.

For example, given that W is "ab",
and S is "abxaba",
return 0, 3, and 4.
"""

# O(n) solution
def Solution(W, S):
    
    lW = len(W)
    lS = len(S)
    
    countW = [0] * 256
    countS = [0] * 256
    
    for i in range(lW):
        (countW[ord(W[i])]) += 1
        (countS[ord(S[i])]) += 1
    retVal = []
    for i in range(lW, lS):
        if compare(countW, countS):
            retVal.append(i - lW)
        countS[ord(S[i])] += 1
        countS[ord(S[i - lW])] -= 1
    if compare(countW, countS):
        retVal.append(lS - lW)
    return retVal
    
    
def compare(ar1, ar2):
    for i in range(256):
        if ar1[i] != ar2[i]:
            return False
    return True
    
    
# Return [0, 3, 4]
print(Solution("ab", "abxaba"))
# Return [1]
print(Solution("le", "helloworld"))