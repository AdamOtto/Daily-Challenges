"""
Given an unsigned 8-bit integer, swap its even and odd bits.
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""
def Solution(ar):
    return (ar & 0b10101010) >> 1 | (ar & 0b01010101) << 1

# Return 01010101
print("{:08b}".format(Solution(0b10101010)))

# Return 11010001
print("{:08b}".format(Solution(0b11100010)))

# Return 10010110
print("{:08b}".format(Solution(0b01101001)))