"""
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

def Solution(s1, s2):
    d = {}
    l1 = len(s1)
    l2 = len(s2)
    if l1 != l2:
        return False

    for i in range(0, l1):
        if s1[i] not in d:
            d[s1[i]] = s2[i]
        elif d[s1[i]] != s2[i]:
            return False
    return True


# s1 = "abc"
# s2 = "bcd"
# s1 = "foo"
# s2 = "bar"
# s1 = "three"
# s2 = "two"
s1 = "abcdefghijklm"
s2 = "nopqrstuvwxyz"
print(Solution(s1, s2))