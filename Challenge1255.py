"""
Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
def Solution(ar, k):
    ar = sorted(ar)
    i = 0
    j = len(ar) - 1
    while i < j:
        if ar[i] + ar[j] < k:
            i += 1
        elif ar[i] + ar[j] > k:
            j -= 1
        else:
            return ar[i], ar[j]
    return False

# Return (7, 10)
print(Solution([10, 15, 3, 7], 17))

# Return False
print(Solution([10, 15, 3, 7], 19))