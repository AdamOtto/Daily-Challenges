"""
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9, or 27 = 5^2 + 1^2 + 1^2.
"""
import math


def Solution(n):
    if n == 0:
        return 0
    """
    l = Helper(n, int( math.sqrt(n) ), [])
    print(l)
    return len(l)
    """
    l = []
    t = int(math.sqrt(n))
    nTemp = n
    while nTemp > 0:
        nTemp = nTemp - pow(t, 2)
        l.append(t)
        t = math.floor(int(math.sqrt(nTemp)))
        if t <= 0:
            t = 1
    #print(l)
    return len(l)


"""
def Helper(n, powNum, lst):

    if n == 0:
        return lst
    elif n < 0:
        return False
    if powNum <= 0:
        return False

    if pow(powNum, 2) > n:
        return Helper(n, int( math.sqrt(n) ), lst)

    lst.append(powNum)

    l1 = Helper(n - pow(powNum, 2), int(math.sqrt( n - pow(powNum, 2) )), lst)
    if type(l1) is bool:
        l1 = Helper(n - pow(powNum, 2), powNum - 1, lst)
        if type(l1) is bool:
            return False
    return l1
"""



in1 = 27
print(Solution(in1))