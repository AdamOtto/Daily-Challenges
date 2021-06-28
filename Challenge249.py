"""
Given an array of integers, find the maximum XOR of any two elements.
"""
import sys
import time

# O(N^2) brute force method
def Solution(ar):
    retVal = -sys.maxsize
    l = len(ar)
    for i in range(0, l):
        for j in range(i + 1, l):
            retVal = max(retVal, ar[i] ^ ar[j])
    return retVal

# Efficent solution.
def Solution2(ar):
    l = len(ar)
    maxVal = 0
    mask = 0
    se = set()

    for i in range(30, -1, -1):
        mask |= (1 << i)
        newMaxVal = maxVal | (1<<i)
        for j in range(l):
            se.add(ar[j] & mask)
        for val in se:
            if newMaxVal ^ val in se:
                maxVal = newMaxVal
        se.clear()
    return maxVal

in1 = [3,10,5,25,2,8]
print(Solution(in1))
in1 = []
for i in range(0, 10001):
    in1.append(i)
start = time.time()
print(Solution(in1))
end = time.time()
print("Solution 1 takes: " + str(end - start) + " secs")


start = time.time()
print(Solution2(in1))
end = time.time()
print("Solution 2 takes: " + str(end - start) + " secs")