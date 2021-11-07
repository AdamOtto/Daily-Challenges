"""
Given a list of integers L, find the maximum length of a
sequence of consecutive numbers that can be formed using elements from L.

For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can
build a sequence [1, 2, 3, 4, 5] which has length 5.
"""

def Solution(ar):
    ar = sorted(ar)
    l = len(ar)
    count = 0
    start = 0
    end = 1
    for i in range(1, l):
        if ar[i - 1] + 1 == ar[i]:
            start = min(i - 1, start)
            end = i
        elif ar[i - 1] == ar[i]:
            start += 1
            end = i
        else:
            count = max(count, end - start + 1)
            start = i
            end = i
    count = max(count, end - start + 1)
    return count

# Return 5
L = [5, 2, 99, 3, 4, 1, 100]
print(Solution(L))

# Return 4 [100,101,102,103]
L = [1,2,4,100,101,102,100,100,103,105]
print(Solution(L))