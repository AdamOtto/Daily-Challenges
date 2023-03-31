"""
You are given an array of arrays of integers, where each array
corresponds to a row in a triangle of numbers.
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down
one row at a time to an adjacent value, eventually ending with an
entry on the bottom row. For example, 1 -> 3 -> 5.
The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
"""
def Solution(ar):
    weights = []
    for i in range(len(ar)):
        weights.append([])
        for j in range(len(ar[i])):
            weights[i].append(0)
    weights[0][0] = ar[0][0]
    for i in range(len(ar) - 1):
        for j in range(len(ar[i])):
            weights[i + 1][j] = max(weights[i + 1][j], weights[i][j] + ar[i + 1][j])
            weights[i + 1][j + 1] = max(weights[i + 1][j + 1], weights[i][j] + ar[i + 1][j + 1])
    return max(weights[-1])

# Return 9
print(Solution([[1], [2, 3], [1, 5, 1]]))

# Return 22
print(Solution([[5], [3, 7], [2, 4, 6], [1,2,3,4]]))

# Return 25
print(Solution([[1], [1, 10], [10, 1, 1], [1,1,1,1], [1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,10,1,1,1]]))