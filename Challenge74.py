'''
Suppose you have a multiplication table that is N by N. That is,
a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1)
(if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of
times X appears as a value in an N by N multiplication table.
'''

#O(n^2) Solution
def BruteForceSolution(N, X):
    t = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j == X:
                t += 1
                
    return t

#O(n) Solution
def Solution(N, X):
    t = 0
    
    #Case for N=1
    if N == 1 and X == 1:
        return 1
    
    #Case for ix1
    if (X <= N):
        t += 1
    
    for i in range(2, N + 1):
        if X % i == 0 and X / i <= N:
            #print(str(X) + "%" + str(i) + " = " + str(X%i))
            t += 1
    return t

"""
for n in range(1, 100):
    for x in range(1, 100):
        t1 = BruteForceSolution(n, x)
        t2 = Solution(n, x)
        if t1 != t2:
            print("N: " + str(n) + ", X: " + str(x) + " returned error: " + str(t1) + " != " + str(t2))
        
"""        
n = 46
x = 96
t1 = BruteForceSolution(n,x)
t2 = Solution(n,x)
print(t1)
print(t2)

