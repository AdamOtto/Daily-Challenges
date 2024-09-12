"""
Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
return 0000 1111 0000 1111 0000 1111 0000 1111.
"""
def Solution(ar):
    return ar ^ 0xffffffff


# Return 00001111000011110000111100001111
print('{:032b}'.format(Solution(0xf0f0f0f0)))
# Return 01010100001100100001000001100111
print('{:032b}'.format(Solution(0xABCDEF98)))