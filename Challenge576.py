"""
Write a function, throw_dice(N, faces, total),
that determines how many ways it is possible to throw N
dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
"""

def throw_dice(N, faces, total):
    mem = [[0 for i in range(total+1)] for j in range(N+1)]
    mem[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, total + 1):
            mem[i][j] = mem[i][j - 1] + mem[i - 1][j - 1]
            if j - faces - 1 >= 0:
                mem[i][j] -= mem[i - 1][j - faces - 1]
    
    return mem[N][total]

# Return 15
print(throw_dice(3,6,7))

# Return 315
print(throw_dice(4,8,20))

# Return 11
print(throw_dice(2,12,14))