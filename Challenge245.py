"""
You are given an array of integers, where each element represents the maximum number
of steps that can be jumped going forward from that element.
Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2,
as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.

"""
import sys

def Solution(ar):
    retVal = Helper(0, ar)
    return retVal

def Helper(cur, jumpList):
    if cur >= len(jumpList) - 1:
        return 0
    elif jumpList[cur] <= 0:
        return sys.maxsize

    t = sys.maxsize
    for i in reversed(range(cur + 1, cur + jumpList[cur] + 1)):
        if i < len(jumpList):
            t = min(t, Helper(i, jumpList))

    return t + 1

in1 = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
print(Solution(in1)) # Ans = 2

in1 = [3,5,0,0,0,5,0,0,3,0,0,1]
print(Solution(in1)) # Ans = 4