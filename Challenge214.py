"""
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""


def Solution(ar):
    if ar == 0:
        return 0
    #print("{0:b}".format(ar))
    temp = 0
    count = 1
    bitLength = ar.bit_length()
    for i in range(bitLength):
        if 1 & ar == 1:
            temp += 1
        else:
            if temp > count:
                count = temp
            temp = 0
        ar >>= 1
    if count > temp:
        return count
    else:
        return temp


in1 = 156
print(Solution(in1))
in1 = 0
print(Solution(in1))
in1 = 15
print(Solution(in1))
in1 = 287
print(Solution(in1))