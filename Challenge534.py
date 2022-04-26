"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar,
which is a palindrome. daily should return false,
since there's no rearrangement that can form a palindrome.
"""

def Solution(ar):
    d = {}
    
    for i in range(len(ar)):
        if ar[i] in d:
            d[ar[i]] += 1
        else:
            d[ar[i]] = 1
    oddFound = False
    for key,val in d.items():
        if val % 2 == 1 and oddFound:
            return False
        elif val % 2 == 1 and not oddFound:
            oddFound = True
    return True            

# Return True
print(Solution("racecar"))
# Return False
print(Solution("daily"))
# Return True
print(Solution("cattaco"))