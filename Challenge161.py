"""
Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
return 0000 1111 0000 1111 0000 1111 0000 1111.
"""

def Solution(in1):
    return 0xffffffff ^ in1


in1 = 0xf0f0f0f0
print('{:032b}'.format(in1))
print('{:032b}'.format(Solution(in1)))

print()

in1 = 0x8afb15fc
print('{:032b}'.format(in1))
print('{:032b}'.format(Solution(in1)))