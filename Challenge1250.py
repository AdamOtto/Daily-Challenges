"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar,
which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""
def Solution(ar):
    d = {}
    for i in range(len(ar)):
        if ar[i] not in d:
            d[ar[i]] = 0
        d[ar[i]] += 1
    even = 0
    odd = 0
    for key,val in d.items():
        if val % 2 == 0:
            even += 1
        else:
            odd += 1
    
    if (odd == 1 or odd == 0):
        return True
    return False

# Return True
print(Solution("carrace"))

# Return False
print(Solution("daily"))