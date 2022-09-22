"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N.
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two),
then [6, 9, 12, ...] (multiples of three), and so on.
Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.
"""

def Solution(ar):
    Primes = [0 for i in range(ar)]
    
    for i in range(2, ar):
        j = 2
        while i * j < ar:
            Primes[i * j] = 1
            j += 1
    
    retVal = []
    for i in range(ar):
        if Primes[i] == 0:
            retVal.append(i)
    return retVal


# Return [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(Solution(30))

# Return [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print(Solution(50))