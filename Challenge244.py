'''
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N.
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two),
then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N,
the unmarked numbers that remain will be prime.

Implement this algorithm.
'''

def Solution(N):
    d = [0] * N
    for i in range(2, N):
        if d[i] == 0:
            j = 2
            while j * i < N:
                d[j * i] = 1
                j += 1
    
    retVal = []
    for i in range(0, N):
        if d[i] == 0:
            retVal.append(i)
    return retVal

print(Solution(100))
print()
print(Solution(300))