"""
Given a string, return the length of the longest palindromic subsequence in the string.

For example, given the following string:

MAPTPTMTPA
Return 7, since the longest palindromic subsequence in the string is APTMTPA.
Recall that a subsequence of a string does not have to be contiguous!

Your algorithm should run in O(n^2) time and space.

Help from: https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
"""

def Solution(ar):
    l = len(ar)
    
    mat = [[0 for i in range(l)] for i in range(l)]
    
    for i in range(l):
        mat[i][i] = 1
        
    for i in range(2, l + 1):
        for j in range(l - i + 1):
            temp = j + i - 1
            if ar[j] == ar[temp] and i == 2:
                mat[j][temp]
            elif ar[j] == ar[temp]:
                mat[j][temp] = mat[j+1][temp-1]+2
            else:
                mat[j][temp] = max(mat[j][temp - 1], mat[j+1][temp])
    return mat[0][l - 1]

# Return 7
print(Solution("MAPTMTPA"))

# Return 11
print(Solution("OABOAACAAODAOE"))