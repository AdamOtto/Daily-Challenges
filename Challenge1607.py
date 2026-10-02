"""
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""
def Solution(s1, s2):
    set1 = set()
    set2 = set()
    
    for s in s1:
        set1.add(s.lower())
    for s in s2:
        set2.add(s.lower())
    
    if len(set1) == len(set2):
        return True
    return False


# Return True
print(Solution("abc", "bcd"))
# Return False
print(Solution("foO", "bar"))
# Return True
print(Solution("abcdefghijklmnopqrs", "Everyone likes me said Caul Shivers the most feared man in the North"))