"""
The ancient Egyptians used to express fractions as a sum of
several terms where each numerator is one.
For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b,
where a < b, into an Egyptian fraction.
"""

def Solution(ar):
    t = ar
    div = 2
    retVal = ""
    while t != 0 and div < 10000:
        if t - (1 / div) >= 0:
            t -= 1 / div
            retVal += "1/" + str(div) + " + "
        div += 1
    return retVal[0: len(retVal) - 2]

# Return 1/4 + 1/18 + 1/468
print(Solution(4 / 13))

# Return 1/7 + 1/140
print(Solution(3 / 20))

# Return 1/2 + 1/4 + 1/20
print(Solution(8 / 10))