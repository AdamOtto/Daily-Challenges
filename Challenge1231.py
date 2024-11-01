"""
The area of a circle is defined as πr^2.
Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2
"""
import random as r

def Solution(ar):
    x = 0
    y = 0
    pInCircle = 0
    for i in range(ar):
        x = r.random()
        y = r.random()
        if pow(x,2) + pow(y, 2) <= 1:
            pInCircle += 1
    return 4 * (pInCircle / ar)


# Generate around 3 ~ 3.3
print(Solution(100))

# Generate around 3.124 ~ 3.25
print(Solution(1000))

# Generate around 3.140 ~ 3.143
print(Solution(1000000))

# Generate around 3.1415 
print(Solution(100000000))