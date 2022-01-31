"""
Implement integer exponentiation. That is, implement the pow(x, y)
function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""

def power(x, y):
    if x == 0:
        return 0
    retVal = 1
    while y > 0:
        if y % 2 >= 1:
            retVal = (retVal * x)
        y = y >> 1
        x = x * x
    return retVal

# Return 1024
print(power(2, 10))

# Return 256
print(power(4, 4))