"""
Given a real number n, find the square root of n.
For example, given n = 9, return 3.
"""

def Solution(n):
    if n < 0:
        return None
    i = 0
    #Whole number check.
    while i * i <= n:
        if i * i == n:
            return i
        i += 1
    return RationalCheck(i, n)

def RationalCheck(i, n):
    upper = i
    lower = i - 1
    cur = (upper + lower) / 2
    curPow = cur * cur
    while round(curPow, 4) != n:
        if curPow < n:
            lower = cur
            cur = (upper + lower) / 2
            curPow = cur * cur
        elif curPow > n:
            upper = cur
            cur = (upper + lower) / 2
            curPow = cur * cur
    return cur

in1 = 9
print(Solution(in1))

in1 = -1
print(Solution(in1))

in1 = 90.25
print(Solution(in1))