"""
You are given an array of nonnegative integers.
Let's say you start at the beginning of the array and
are trying to advance to the end.
You can advance at most, the number of steps that you're currently on.
Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1],
we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0],
we can't reach the end, so return false.
"""
def Solution(ar):
    q = []
    q.append( (0,0) )
    retVal = len(ar) + 1
    while len(q) > 0:
        cur = q.pop()
        for i in range(1, ar[cur[0]] + 1):
            if cur[0] + i < len(ar) and ar[cur[0] + i] > 0:
                if cur[0] + i == len(ar) - 1:
                    return True
                else:
                    q.append( (cur[0] + i, cur[1] + 1) )
    return False
# Return True
print(Solution([1, 3, 1, 2, 0, 1]))
# Return False
print(Solution([1, 2, 1, 0, 0]))