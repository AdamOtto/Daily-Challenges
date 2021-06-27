"""
Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.
"""

def Solution_ar1_lessThan_ar2(ar1, ar2):
    return bool((ar1 - ar2) >> 31)

print(Solution_ar1_lessThan_ar2(10,1))
print(Solution_ar1_lessThan_ar2(1,10))
print(Solution_ar1_lessThan_ar2(-10,1))
print(Solution_ar1_lessThan_ar2(65412, 1243))

print()

def Solution_ar1_greaterThan_ar2(ar1, ar2):
    return bool((ar2 - ar1) >> 31)
print(Solution_ar1_greaterThan_ar2(10,1))
print(Solution_ar1_greaterThan_ar2(1,10))
print(Solution_ar1_greaterThan_ar2(-10,1))
print(Solution_ar1_greaterThan_ar2(65412, 1243))