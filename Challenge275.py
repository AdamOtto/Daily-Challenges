"""
The "look and say" sequence is defined as follows:
beginning with the term 1, each subsequent term visually describes
the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""

def Solution(N):
    if N <= 0:
        return False
    if N == 1:
        return "1"
    cur = 1
    old = [1]
    new = [1]
    
    for i in range(1, N):
        old = new[:]
        new = []
        cur = old[0]
        count = 1
        for j in range(1, len(old)):
            if old[j] == cur:
                count += 1
            else:
                new.append(count)
                new.append(cur)
                cur = old[j]
                count = 1
        new.append(count)
        new.append(cur)
        
    retVal = ""
    for c in new:
        retVal += str(c)
    return retVal

print(Solution(1))
print(Solution(2))
print(Solution(3))
print(Solution(4))
print(Solution(5))
print(Solution(6))
print(Solution(7))
print(Solution(8))
print(Solution(9))