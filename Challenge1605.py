"""
You are given a 2 x N board, and instructed to
completely cover the board with the following shapes:

Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.

For example, if N = 4, here is one possible configuration,
where A is a domino, and B and C are trominoes.

A B B C
A B C C
Given an integer N, determine in how many ways this task is possible.
"""

def Solution(N):
    return Helper(0, N)

def Helper(cur, N):
    if cur == N:
        return 1
    temp = 0
    # domino positioned vertically (||)
    if cur + 1 <= N:
        temp += Helper(cur + 1, N)
    # domino positioned horizontally (Always place another underneath (=)).
    if cur + 2 <= N:
        temp += Helper(cur + 2, N)
    # Tromino (paired with another (┌ ┘,└ ┐) )(Two configurations).
    if cur + 3 <= N:
        temp += Helper(cur + 3, N) * 2
        j = 5
        # This configurations can be expanded infinitely, increasing by two each time by adding another horizontal domino.
        while j <= N:
            temp += Helper(cur + j, N) * 2
            j += 2
    # Two trominoes and a domino place horizontally in between them (two possible configurations (┌ --┐, └--┘) ).
    if cur + 4 <= N:
        temp += Helper(cur + 4, N) * 2
        j = 6
        # This configurations can be expanded infinitely, increasing by two each time by adding another horizontal domino.
        while j <= N:
            temp += Helper(cur + j, N) * 2
            j += 2
    return temp

# Return 1
print(Solution(1))
# Return 2
print(Solution(2))
# Return 5
print(Solution(3))
# Return 11
print(Solution(4))
# Return 1255
print(Solution(10))