"""
Pascal's triangle is a triangular array of integers
constructed with the following formula:

 - The first row consists of the number 1.
 - For each subsequent row, each element is the sum of the numbers
   directly above it, on either side.

For example, here are the first few rows:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?
"""

def Solution(k):
    retVal = []
    C = 1
    for i in range(1, k + 1):
        retVal.append(C)
        C = int(C * (k - i) / i)
    return retVal


print(Solution(1))
print(Solution(2))
print(Solution(3))
print(Solution(4))
print(Solution(5))
print(Solution(6))
print(Solution(7))
print(Solution(8))
print(Solution(9))
print(Solution(10))