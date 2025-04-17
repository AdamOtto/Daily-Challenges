"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""
def Solution(n):
    if n <= 0:
        return 0
    i = 10
    k = n
    
    while k > 0:
        i += 9
        k -= 1
    return i

# Return 19
print(Solution(1))
# Return 28
print(Solution(2))
# Return 37
print(Solution(3))
# Return 55
print(Solution(5))
# Return 910
print(Solution(100))