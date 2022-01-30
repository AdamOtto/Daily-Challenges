"""
Given a 32-bit positive integer N, determine whether
it is a power of four in faster than O(log N) time.
"""
import math

# O(1) time and space
def Solution(N):
    t1 = math.log(N) / math.log(4)
    t2 = math.floor(math.log(N) / math.log(4))
    return t1 == t2

# Return True
print(Solution(4))
# Return False
print(Solution(8))
# Return True
print(Solution(16))
# Return False
print(Solution(32))
# Return True
print(Solution(64))
# Return False
print(Solution(math.pow(4, 9) + 1))
# Return True
print(Solution(math.pow(4, 9)))