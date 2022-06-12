"""
You are given a 2-d matrix where each cell
represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down,
find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is
0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""
def Solution(ar, cur = None):
    if cur == None:
        cur = (0, 0)
    if cur == ( len(ar) - 1, len(ar[0]) - 1 ):
        return ar[cur[0]][cur[1]]
    elif cur[0] >= len(ar) or cur[1] >= len(ar[0]):
        return -1
    
    return max(ar[cur[0]][cur[1]] + Solution(ar, (cur[0] + 1, cur[1])), ar[cur[0]][cur[1]] + Solution(ar, (cur[0], cur[1] + 1)))

# Return 12
in1 = [[0, 3, 1, 1],
       [2, 0, 0, 4],
       [1, 5, 3, 1]]
print(Solution(in1))

# Return 19
in1 = [[1, 2, 3, 2, 5],
       [1, 1, 0, 4, 3],
       [1, 2, 2, 5, 2]]
print(Solution(in1))