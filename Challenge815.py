"""
The area of a circle is defined as πr^2.
Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random

def Solution():
    iterations = 1000000
    count = 0
    x = 0.0
    y = 0.0
    for i in range(0, iterations):
        x = random.uniform(-.5, .5)
        y = random.uniform(-.5, .5)
        if (x*x) + (y*y) <= 0.25:
            count += 1
    return "{:.3f}".format(( 4 * (count / iterations)))


print(Solution())