"""
Let's define a "sevenish" number to be one which is either a power of 7,
or the sum of unique powers of 7. The first few sevenish numbers
are 1, 7, 8, 49, and so on.

Create an algorithm to find the nth sevenish number.
"""

def Solution(ar):
    powNum = 0
    temp = ar
    retVal = 0
    while temp > 0:
        if temp & 1 == 1:
            retVal += pow(7, powNum)
        temp = temp >> 1
        powNum += 1
    return retVal

for i in range(0, 16):
    print(Solution(i))