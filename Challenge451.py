"""
Implement the function fib(n), which returns the nth number
in the Fibonacci sequence, using only O(1) space.
"""

def fib(n):
    if n <= 0:
        return 0
    if n <= 1:
        return 1
    last1 = 0
    last2 = 1
    cur = last1 + last2
    for i in range(n - 2):
        last1 = last2
        last2 = cur
        cur = last1 + last2
    return cur

# Return 5
print(fib(5))

# Return 8
print(fib(6))

# Return 55
print(fib(10))