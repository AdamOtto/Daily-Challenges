"""
Given an even number (greater than 2), return two prime
numbers whose sum will be equal to the given number.

A solution will always exist.
See Goldbach’s conjecture.

Example:
Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d]
is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""


#Source wikipedia Primality test
def isprime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
def Solution(t):
    
    if t % 2 != 0:
        return False
    
    d = {}
    
    for i in range(2, t):
        if isprime(i):
            d[i] = 0
            if t-i in d or isprime(t-i):
                return (i, t-i)
    return False
    


print(Solution(6))
print(Solution(4))
print(Solution(1902))
print(Solution(6002))
print(Solution(99292))  