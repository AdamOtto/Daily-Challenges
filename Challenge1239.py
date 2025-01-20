"""
Implement division of two positive integers without using
the division,multiplication, or modulus operators.

Return the quotient as an integer, ignoring the remainder.
"""

def Solution(dividend, divisor):
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return quotient

# Return 2
print(Solution(4, 2))

# Return 4
print(Solution(18, 4))

# Return 1000
print(Solution(1000, 1))