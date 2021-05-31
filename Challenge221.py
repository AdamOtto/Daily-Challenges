"""
Let's define a "sevenish" number to be one which is either a power of 7,
or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on.

Create an algorithm to find the nth sevenish number.
"""

def Solution(ar):
    if ar <= 0:
        return 0
    count = 0
    retVal = 0
    while ar != 0:
        if 1 & ar == 1:
            retVal += pow(7, count)
        ar >>= 1
        count += 1
    return retVal

in1 = 0
print(Solution(in1))
in1 = 1
print(Solution(in1))
in1 = 2
print(Solution(in1))
in1 = 3
print(Solution(in1))
in1 = 4
print(Solution(in1))
in1 = 5
print(Solution(in1))
in1 = 6
print(Solution(in1))
in1 = 7
print(Solution(in1))