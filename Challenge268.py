'''
Given a 32-bit positive integer N,
determine whether it is a power of four in faster than O(log N) time.
'''
import math

# O(1) time and space
def Solution(N):
    t1 = math.log(N) / math.log(4)
    t2 = math.floor(math.log(N) / math.log(4))
    return t1 == t2

print(Solution(4))
print(Solution(8))
print(Solution(16))
print(Solution(32))
print(Solution(64))
print(Solution(math.pow(4, 9) + 1))
print(Solution(math.pow(4, 9)))