"""
Given an unsigned 8-bit integer, swap its even and odd bits.
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""

def Solution(ar):
    return (ar & 0b10101010) >> 1 | (ar & 0b01010101) << 1

# Return (0)1010101
print("{0:b}".format(Solution(0b10101010)))

# Return 11110000
print("{0:b}".format(Solution(0b11110000)))

# Return 10110001
print("{0:b}".format(Solution(0b01110010)))