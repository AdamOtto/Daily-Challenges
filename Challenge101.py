'''
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
'''

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
    

t = 5
h = Solution(t)
print(h)
t = 4
h = Solution(t)
print(h)
t = 6036
h = Solution(t)
print(h)
t = 1000000
h = Solution(t)
print(h)  