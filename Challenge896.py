"""
Implement division of two positive integers without using the division,
multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder.
"""

def Solution(dividend, divisor):
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return quotient
    
# Return 2022
print(Solution(4044, 2))

# Return 5
print(Solution(15, 3))

# Return 3
print(Solution(15, 4))