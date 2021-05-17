"""
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

    if n is even, the next number in the sequence is n / 2
    if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?

Results:
Testing all numbers from 1 to 1000000 returns a value of 1.
Anything below 1 or decimal numbers will not work.
The highest sequence is 524 for n = 837799
"""


def Solution(ar):
    count = 0
    while not ar == 1:
        count += 1
        if ar % 2 == 0:
            ar = ar / 2
        else:
            ar = (3*ar) + 1
    return count

highest = 0
index = 0
for i in range(1, 1000001):
    t = Solution(i)
    if t > highest:
        highest = t
        index = i
print("Highest sequence: " + str(highest) + ", at index: " + str(index))