"""
Given a list, sort it using this method:
reverse(lst, i, j)
which reverses lst from i to j.
"""

# O(n) time.
def reverse(lst, i, j):
    l = len(lst)

    if i >= j:
        return
    indexI = i
    indexJ = j
    while indexI < indexJ:
        t = lst[indexI]
        lst[indexI] = lst[indexJ]
        lst[indexJ] = t
        indexI += 1
        indexJ -= 1
    return

in1 = [0,1,2,3,4,5,6,7,8,9,10]
i = 0
j = 5

print(in1)
reverse(in1, i, j)
print(in1)