"""
Given an array of integers, determine whether it contains
a Pythagorean triplet.

Recall that a Pythogorean triplet (a, b, c)
is defined by the equation a2+ b2= c2.
"""

def Solution(ar):
    l = len(ar)
    if l < 2:
        return False
    d = set()
    for i in range(l):
        d.add(ar[i] ** 2)
    
    for i in range(l):
        for j in range(i,l):
            if (ar[i] ** 2) + (ar[j] ** 2) in d:
                return True
    return False

# Return True
print(Solution([1,2,3,4,5,6,7]))

# Return False
print(Solution([2,3,4]))

# Return False
print(Solution([100,13,14,52,24,13,62,35,87]))

# Return True
print(Solution([16, 10, 95, 30, 21, 45, 34, 109, 11]))