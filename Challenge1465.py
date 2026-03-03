"""
In front of you is a row of N coins, with values v1, v1, ..., vn.
You are asked to play the following game. You and an opponent take turns choosing either
the first or last coin from the row, removing it from the row, and receiving the value of the coin.
Write a program that returns the maximum amount of money you can win with certainty,
if you move first, assuming your opponent plays optimally.
"""
def Solution(ar):
    n = len(ar)
    table = [[0 for i in range(n)]
             for i in range(n)]
    
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
            x = 0
            if((i + 2) <= j):
                x = table[i + 2][j]
            y = 0
            if((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            z = 0
            if(i <= (j - 2)):
                z = table[i][j - 2]
            table[i][j] = max(ar[i] + min(x, y),
                              ar[j] + min(y, z))
    return table[0][n - 1]

# Return 12
print(Solution([1,1,10,1,1,1]))

# Return 28
print(Solution([12,15,13,13]))