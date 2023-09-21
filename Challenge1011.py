"""
Find the maximum of two numbers without using
any if-else statements, branching, or direct comparisons.
"""

def Solution_ar1_lessThan_ar2(ar1, ar2):
    temp = (ar1 - ar2)
    temp = temp >> 63
    temp = bool(temp)
    return bool((ar1 - ar2) >> 63)


# Return True
print(Solution_ar1_lessThan_ar2(1,2))
print(Solution_ar1_lessThan_ar2(100000001,202020202020202))

# Return False
print(Solution_ar1_lessThan_ar2(2,1))
print(Solution_ar1_lessThan_ar2(202020202020202, 100000001))