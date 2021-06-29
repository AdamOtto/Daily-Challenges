"""
Given a array of numbers representing the stock prices of a company
in chronological order, write a function that calculates the maximum
profit you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10],
you should return 5, since you could buy the stock at 5 dollars
and sell it at 10 dollars.
"""
import random
import time

# Brute force method, O(N^2)
def Solution1(ar):
    retVal = 0
    l = len(ar)
    for i in range(0, l):
        for j in range(i + 1, l):
            retVal = max(retVal, ar[j] - ar[i])
    return retVal

# O(N) method
def Solution2(ar):
    l = len(ar)
    minElement = 0
    retVal = 0

    for i in range(1, l):
        retVal = max(retVal, ar[i] - ar[minElement])
        if ar[i] < ar[minElement]:
            minElement = i
    return retVal


in1 = [9, 11, 8, 5, 7, 10]
print(Solution1(in1))
print(Solution2(in1))
print()

in1 = [1000, 501, 500, 1000, 5, 2, 500]
print(Solution1(in1))
print(Solution2(in1))
print()

in1 = []
for i in range(0, 10001):
    in1.append(random.randint(1,10000))

start = time.time()
print(Solution1(in1))
end = time.time()
print("Solution 1 takes: " + str(end - start) + " secs")

start = time.time()
print(Solution2(in1))
end = time.time()
print("Solution 2 takes: " + str(end - start) + " secs")
