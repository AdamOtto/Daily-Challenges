"""
You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down,
find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""
def Solution(ar):
    m = len(ar)
    n = len(ar[0])
    
    count = [[0 for i in range(n) ] for j in range(m)]
    count[0][0] = ar[0][0]
    q = []
    q.append( (0, 0) )
    while len(q) > 0:
        temp = q.pop(0)
        if temp[0] + 1 < m:
            count[temp[0] + 1][temp[1]] = max(count[temp[0] + 1][temp[1]], ar[temp[0] + 1][temp[1]] + count[temp[0]][temp[1]])
            q.append( (temp[0] + 1, temp[1]) )
        if temp[1] + 1 < n:
            count[temp[0]][temp[1] + 1] = max(count[temp[0]][temp[1] + 1], ar[temp[0]][temp[1] + 1] + count[temp[0]][temp[1]])
            q.append( (temp[0], temp[1] + 1) )
    return count[m - 1][n - 1]

# Return 12
in1 = [ [0,3,1,1],
        [2,0,0,4],
        [1,5,3,1]]
print(Solution(in1))

# Return 20
in1 = [ [0,3,1,1,4,1],
        [2,3,4,4,2,1],
        [1,5,3,2,1,1],
        [10,1,1,2,1,1]]
print(Solution(in1))