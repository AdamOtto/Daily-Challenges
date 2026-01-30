"""
You are given an array of arrays of integers,
where each array corresponds to a row in a triangle of numbers.
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value,
eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5.
The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
"""
def Solution(ar, lvl = 0, i = 0):
    if lvl == len(ar) - 1:
        return ar[lvl][i]
    return max(ar[lvl][i] + Solution(ar, lvl + 1, i), ar[lvl][i] + Solution(ar, lvl + 1, i + 1))


# Returns 9 (1 + 3 + 5)
print(Solution([[1], [2, 3], [1, 5, 1]]))

# Return 13
print(Solution([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]))

# Return 35
print(Solution([[1], [1, 10], [10, 1, 1], [10,1,1,1], [1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1,1], [1,1,1,1,10,1,1,1]]))