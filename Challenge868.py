"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar,
which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""
def Solution(ar):
    d = {}
    for a in ar:
        if a not in d:
            d[a] = 0
        d[a] += 1
    odds = 0
    for key, val in d.items():
        if val % 2 >= 1:
            odds += 1
        if odds >= 2:
            return False
    return True

# Return True
print(Solution("carrace"))
# Return False
print(Solution("Hello World"))
# Return True
print(Solution("always say law"))