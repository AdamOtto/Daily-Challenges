"""
Implement integer division without using the division operator.
Your function should return a tuple of (dividend, remainder) and it should take two numbers,
the product and divisor.

For example, calling divide(10, 3) should return (3, 1)
since the divisor is 3 and the remainder is 1.

Bonus: Can you do it in O(log n) time?
"""
import math
import time

# O(n) Solution
def Solution1(dividen, divisor):
    copy = dividen
    count = 0
    while copy >= divisor and copy >= 0:
        copy -= divisor
        count += 1
    return (count, copy)

# O(logn)
def Solution2(dividen, divisor):
    low = 0
    high = dividen
    mid = int(math.floor((low + high) / 2))
    while low < high:
        if int(mid * divisor) == dividen:
            return (mid, 0)

        elif int(mid * divisor) > dividen:
            high = mid - 1
            mid = int(math.floor((low + high) / 2))
        else:
            low = mid + 1
            mid = int(math.floor((low + high) / 2))
    if int(mid * divisor) > dividen:
        mid -= 1
    return (mid, dividen - int(mid * divisor))

print(Solution1(10, 3))
print(Solution2(10, 3))

print(Solution1(16, 4))
print(Solution2(16, 4))

start = time.time()
print(Solution1(10000000, 1))
end = time.time()
print("Code took", end - start, "second(s) to execute")
start = time.time()
print(Solution2(10000000, 1))
end = time.time()
print("Code took", end - start, "second(s) to execute")
