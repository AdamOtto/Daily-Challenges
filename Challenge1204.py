"""
Given n numbers, find the greatest
common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""
def Solution(ar):
    l = len(ar)
    largest = max(ar)
    denomFound = True
    for i in reversed(range(largest)):
        denomFound = True
        for j in range(l):
            if ar[j] % i != 0:
                denomFound = False
                break
        if denomFound:
            return i
    return False
    
# Return 14
print(Solution([42, 56, 14]))

# Return 1
print(Solution([24, 29, 30]))