"""
Given a list of numbers and a number k, return
whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def Solution(ar, k):
    l = len(ar)
    if l <= 1:
        return False
    d = {}
    d[ar[0]] = ar[0]
    for i in range(1, l):
        if k - ar[i] in d:
            return True
        else:
            d[ar[i]] = ar[i]
    return False

# Return True
print(Solution([10,15,3,7], 17))

# Return True
print(Solution([1,2,3], 5))

# Return False
print(Solution([1,2,3], 6))