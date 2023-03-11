"""
Given an integer list where each number represents the number
of hops you can make, determine whether you can reach to
the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""
def Solution(ar, cur = 0):
    if ar[cur] == 0 and cur != len(ar) - 1:
        return False
    elif cur == len(ar) - 1:
        return True
    if cur >= len(ar):
        return False
    
    for i in reversed(range(1, ar[cur] + 1)):
        if Solution(ar, cur + i):
            return True
    return False


# Return True
print(Solution([2, 0, 1, 0]))

# Return False
print(Solution([1, 1, 0, 1]))

# Return True
print(Solution([1,2,0,4,5,0,0,0,0,0]))