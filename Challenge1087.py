"""
Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""
def Solution(A, B):
    if len(A) != len(B):
        return False
    l = len(A)
    iA = 0
    
    for i in range(l):
        if A[i] == B[0]:
            iA = i
            break
    
    for i in range(l):
        if A[iA] != B[i]:
            return False
        
        iA += 1
        if iA >= l:
            iA = 0
    return True

# Return True
print(Solution("abcde", "cdeab"))
# Return False
print(Solution("abc", "acb"))