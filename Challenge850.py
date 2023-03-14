"""
Given a set of characters C and an integer k, a De Bruijn sequence is a cyclic
sequence in which every possible k-length string of characters in C occurs exactly once.

For example, suppose C = {0, 1} and k = 3. Then our sequence should contain
the substrings {'000', '001', '010', '011', '100', '101', '110', '111'},
and one possible solution would be 00010111.

Create an algorithm that finds a De Bruijn sequence.

Got help for code from:
https://www.geeksforgeeks.org/de-bruijn-sequence-set-1/
"""
import math

seen = set()
edges = []

def dfs(node, k, A):
    for i in range(k):
        str = node + A[i]
        if (str not in seen):
            seen.add(str)
            dfs(str[1:], k, A)
            edges.append(i)

def Solution(n, A):
    # Clearing global variables
    seen.clear()
    edges.clear()
    k = len(A)
    startingNode = A[0] * (n - 1)
    dfs(startingNode, k, A)
     
    S = ""
     
    # Number of edges
    l = int(math.pow(k, n))
    for i in range(l):
        S += A[edges[i]]
         
    S += startingNode
    
    if S[:2] == S[len(S) - 2 :]:
        return S[0:len(S) - 2]
    return S

# Return 00111010
A = "01"
print(Solution(3, A))

# Return accbbcabaa
A = "abc"
print(Solution(2, A))

# Return aacccbcbbbccabcacbabbacaaba
A = "abc"
print(Solution(3, A))

# Return wzzyyzxyxxzwywxww
A = "wxyz"
print(Solution(2, A))

# Return rrvvvuvuuuvvtuvtvutuutvttutttvvsuvstvsvusuustusvtsutsttsvssusstsssvvruvrtvrsvrvuruurtursurvtrutrttrstrvsrusrtsrssrvrrurrtrrsr
A = "rstuv"
print(Solution(3, A))