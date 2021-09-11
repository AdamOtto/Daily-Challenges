"""
You are going on a road trip, and would like to create a suitable music playlist.
The trip will require N songs, though you only have M songs downloaded, where M < N.
A valid playlist should select each song at least once, and guarantee a
buffer of B songs between repeats.

Given N, M, and B, determine the number of valid playlists.
"""

def Solution(N, M, B):
    if N <= M:
        return False
    
    mat = [[0 for j in range(M + 1)] for i in range(N + 1)]
    mat[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            mat[i][j] = mat[i - 1][j - 1] * (M - (j - 1)) + mat[i - 1][j] * max(j - B, 0)
    
    return mat[N][M]

# Return 2
print(Solution(3,2,1))

# Return 6
print(Solution(5,3,2))

# Return 24
print(Solution(5,4,3))

# Return 216720
print(Solution(10,6,3))