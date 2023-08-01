"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, so an island is a group of 1s
that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""
def printMatrix(m):
    for i in range(0, len(m)):
        t = ""
        for j in range(0, len(m[i])):
            t += str(m[i][j]) + " "
        print(t)


def Solution(in1):
    d = {}
    count = 0
    for i in range(0, len(in1)):
        for j in range(0, len(in1[i])):
            if (i, j) not in d and in1[i][j] == 1:
                t = findNeighboors(in1, i, j)
                d[(i, j)] = count
                while len(t) > 0:
                    x, y = t.pop()
                    # print("x: " + str(x) + ", y: " + str(y))
                    if (x, y) not in d:
                        d[(x, y)] = count
                        temp = findNeighboors(in1, x, y)
                        for te in temp:
                            t.append(te)
                count += 1

    print(count)


def findNeighboors(in1, i, j):
    maxi = len(in1)
    maxj = len(in1[0])
    t = []
    if i + 1 < maxi and in1[i + 1][j]:
        t.append((i + 1, j))
    if j + 1 < maxj and in1[i][j + 1]:
        t.append((i, j + 1))
    if i - 1 >= 0 and in1[i - 1][j]:
        t.append((i - 1, j))
    if j - 1 >= 0 and in1[i][j - 1]:
        t.append((i, j - 1))
    return t

# Return 5
in1 = [
    [1, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 1]
]
printMatrix(in1)
Solution(in1)

print()

# Return 9
in1 = [
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0]
]
printMatrix(in1)
Solution(in1)