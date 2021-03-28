"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar.
daily should return false, since there's no rearrangement that can form a palindrome.
"""

def Solution(pal):
    d = {}

    for s in pal:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    odd = 0
    for key,value in d.items():
        if value % 2 > 0:
            odd += 1

    if odd > 1:
        return False
    return True


in1 = "carrace"
#in1 = "aebyaybea"
print(Solution(in1))