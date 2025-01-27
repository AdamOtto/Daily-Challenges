"""
Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""
def Solution(A, B):
    if len(A) != len(B):
        return False
    temp = A
    for i in range(len(B) + 1):
        if temp == B:
            return True
        else:
            temp = temp[1:] + temp[0]
    return False

# Return True
print(Solution("abc", "cab"))
# Return False
print(Solution("abc", "acb"))