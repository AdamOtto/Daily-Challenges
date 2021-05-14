'''
Implement division of two positive integers without using the division,
multiplication, or modulus operators. Return the quotient as an integer,
ignoring the remainder.
'''

def Solution(dividend, divisor):
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return quotient
    
in1 = 4042
in2 = 2
print(Solution(in1, in2))