"""
We say a number is sparse if there are no adjacent ones in its binary representation.
For example, 21 (10101) is sparse, but 22 (10110) is not.
For a given input N, find the smallest sparse number greater than or equal to N.
Do this in faster than O(N log N) time.
"""

def Solution(ar):
    l = []
    while ar != 0:
        l.append(ar & 1)
        ar >>= 1
    l.append(0)
    n = len(l)
    last = 0
    for i in range(1, n - 1):
        if l[i] == 1 and l[i - 1] == 1 and l[i + 1] != 1:
            l[i + 1] = 1
            for j in range(i, last - 1, -1):
                l[j] = 0
        last = i + 1
    retVal = 0
    for i in range(n):
        retVal += l[i] * (1 << i)
    return retVal

# Return 21
print(Solution(21))

# Return 42
print(Solution(22))

# Return 164
print(Solution(100))