"""
You are given N identical eggs and access to a building with k floors.
Your task is to find the lowest floor that will cause an egg to break,
if dropped from that floor. Once an egg breaks, it cannot be dropped again.
If an egg breaks when dropped from the xth floor, you can assume it will
also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take,
in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor,
beginning with the first, until we reach the fifth floor, so our solution will be 5.
"""
import sys

def Solution(eggs, floors):
    eggFloor = [[0 for i in range(floors + 1)] for j in range(eggs + 1)]

    for i in range(1, eggs + 1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0

    for i in range(1, floors + 1):
        eggFloor[1][i] = i

    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            eggFloor[i][j] = sys.maxsize
            for k in range(1, j + 1):
                temp = 1 + max(eggFloor[i - 1][k - 1], eggFloor[i][j - k])
                if temp < eggFloor[i][j]:
                    eggFloor[i][j] = temp
    return eggFloor[eggs][floors]

N = 1
k = 5
print(Solution(N, k))

N = 2
k = 10
print(Solution(N, k))

N = 2
k = 36
print(Solution(N, k))

N = 50
k = 500
print(Solution(N, k))