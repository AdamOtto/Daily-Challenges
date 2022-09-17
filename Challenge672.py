"""
You are given an array of arrays of integers, where each array corresponds
to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row
at a time to an adjacent value, eventually ending with an entry on the bottom row.
For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
"""
def Solution(ar, cur = (0,0)):
    if cur[0] >= len(ar):
        return 0
    if cur[1] >= len(ar[cur[0]]):
        return 0
    return ar[cur[0]][cur[1]] + max(Solution(ar, (cur[0] + 1, cur[1])), Solution(ar, (cur[0] + 1, cur[1] + 1)))
    
# Return 9
print(Solution([[1], [2, 3], [1, 5, 1]]))

# Return 7
print(Solution([[1], [4, 1], [-10, 2, 1], [-2, -1, -3, 4]]))