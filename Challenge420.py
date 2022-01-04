"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

# Inefficient solution
def Solution1(n):
    if n <= 0:
        return 0
    k = n
    i = 18
    while k > 0:
        i += 1
        st = str(i)
        tot = 0
        for s in st:
            tot += int(s)
        if tot == 10:
            k -= 1
    return i
        
# More efficient solution
def Solution2(n):
    if n <= 0:
        return 0
    i = 10
    k = n
    
    while k > 0:
        i += 9
        k -= 1
    return i
    

print(Solution1(1))
print(Solution1(2))
print(Solution1(3))
print(Solution1(5))
print()
print(Solution2(1))
print(Solution2(2))
print(Solution2(3))
print(Solution2(5))