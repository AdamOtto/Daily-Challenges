'''
A regular number in mathematics is defined as one which evenly divides some power of 60.
Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep
time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns,
in order, the first N regular numbers.

The first few regular numbers are:
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60

**Notes**
regular number = 2^i * 3^j * 5^k
and 
60^x % regular number = 0
'''

def Solution(N):
    
    h = [1] * N
    n2 = 2
    n3 = 3
    n5 = 5
    i = j = k = 0
    n = 1
    while n < N:
        h[n] = min(n2, n3, n5)
        
        if n2 == h[n]:
            i += 1
            n2 = 2 * h[i]
        if n3 == h[n]:
            j += 1
            n3 = 3 * h[j]
        if n5 == h[n]:
            k += 1
            n5 = 5 * h[k]
        if valIsDivisorOf60(i, j, k, h[n]):
            n += 1
    
    return h

def valIsDivisorOf60(i, j, k, val):
    p = max(int(i / 2), j, k, 1)
    for pi in range(1, p + 1):
        if pow(60, pi) % val == 0:
            return True
    return False

def getNextMin(n2, n3, n5, val):
    if val == n2:
        return min(n3, n5)
    if val == n3:
        return min(n2, n5)
    if val == n5:
        return min(n2, n3)
        

t = Solution(30)
print(str(len(t)) + ": " + str(t))
print()
t = Solution(50)
print(str(len(t)) + ": " + str(t))
print()
t = Solution(75)
print(str(len(t)) + ": " + str(t))