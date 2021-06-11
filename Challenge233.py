"""
Implement the function fib(n).
Which returns the nth number in the Fibonacci sequence.
Using only O(1) space.
"""

def Solution(ar):
    if ar <= 0:
        return 0
    if ar <= 1:
        return 1
    last1 = 0
    last2 = 1
    cur = last1 + last2
    for i in range(ar - 2):
        last1 = last2
        last2 = cur
        cur = last1 + last2
    return cur

print(str(Solution(0)) + ", " + str(Solution(1)) + ", " + str(Solution(2)) + ", " + str(Solution(3)) + ", " + str(Solution(4)) + ", " +
      str(Solution(5)) + ", " + str(Solution(6)) + ", " + str(Solution(7)) + ", " + str(Solution(8)) + ", " + str(Solution(9))
      + ", " + str(Solution(10)))