"""
In linear algebra, a Toeplitz matrix is one in which the elements on any
given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
Write a program to determine whether a given input is a Toeplitz matrix.
"""
def Solution(ar):
    l1 = len(ar)
    l2 = len(ar[0])
    for i in range(0, l1):
        if not Helper(ar, ar[i][0], i, 0, l1, l2):
            return False

    for i in range(1, l2):
        if not Helper(ar, ar[0][i], 0, i, l1, l2):
            return False
    return True

def Helper(ar, match, i, j, l1, l2):
    while i < l1 and j < l2:
        if ar[i][j] != match:
            return False
        i += 1
        j += 1
    return True

# Return True
in1 = [ [1,2,3,4,8],
        [5,1,2,3,4],
        [4,5,1,2,3],
        [7,4,5,1,2]]
print(Solution(in1))

# Return False
in1 = [ [1,2,3,4,8],
        [5,1,2,3,4],
        [4,5,2,2,3],
        [7,4,5,1,2]]
print(Solution(in1))