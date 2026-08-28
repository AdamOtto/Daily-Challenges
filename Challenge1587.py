"""
You are given an array of integers, where each element represents
the maximum number of steps that can be jumped going forward from that element.
Write a function to return the minimum number of jumps you must take
in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9],
you should return 2, as the optimal solution involves
jumping from 6 to 5, and then from 5 to 9.
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
                    retVal = min(retVal, cur[1] + 1)
                else:
                    q.append( (cur[0] + i, cur[1] + 1) )
    if retVal == len(ar) + 1:
        return None
    return retVal

# Return 2
print(Solution([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]))
# Return None
print(Solution([1,2,0,0,3,0,0,4]))
# Return 3
print(Solution([1,2,0,3,0,0,4]))