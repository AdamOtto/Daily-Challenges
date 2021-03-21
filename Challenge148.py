"""
Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""


def Solution(n):
    if n <= 0:
        return False

    gray = ["0","1"]
    if n == 1:
        return gray

    retVal = []

    for i in range(1, n):
        retVal = []
        l = len(gray)
        for j in range(0, l):
            retVal.append("0" + gray[j])
        for j in reversed(range(0, l)):
            retVal.append("1" + gray[j])
        gray = retVal
    return retVal


in1 = 4
print(Solution(in1))