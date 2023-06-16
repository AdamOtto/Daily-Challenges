"""
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""
def Solution(ar):
    denom = min(ar)
    l = len(ar)
    while denom >= 1:
        breakLoop = True
        for i in range(l):
            if ar[i] % denom >= 1:
                breakLoop = False
                break
        if breakLoop:
            break
        denom -= 1
    return denom

# Return 14
print(Solution([42, 56, 14]))
# Return 1
print(Solution([3,5,7]))
# Return 2
print(Solution([102,508,298]))