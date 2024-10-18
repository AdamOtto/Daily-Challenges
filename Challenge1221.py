"""
Implement the function fib(n),
which returns the nth number in the
Fibonacci sequence, using only O(1) space.
"""
def Solution(ar):
    f1 = 0
    f2 = 1
    if ar <= 1:
        return f1
    elif ar == 2:
        return f2
    
    for i in range(3, ar + 1):
        t = f2
        f2 = t + f1
        f1 = t
    
    return f2


# Return 1
print(Solution(2))
# Return 2
print(Solution(4))
# Return 5
print(Solution(6))
# Return 13
print(Solution(8))
# Return 34
print(Solution(10))
# Return 4181
print(Solution(20))