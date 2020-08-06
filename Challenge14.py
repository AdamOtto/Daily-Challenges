"""
The area of a circle is defined as πr^2
Estimate π to 3 decimal places using a Monte Carlo method.
"""
import random

def MonteCarloUnitCircle (iterations):
    count = 0
    x = 0.0
    y = 0.0
    for i in range(0, iterations):
        x = random.uniform(-.5, .5)
        y = random.uniform(-.5, .5)
        #print(str(x) + " * " + str(x) + " = " + str(x*x))
        if (x*x) + (y*y) <= 0.25:
            count += 1
    #print(count)
    #print(iterations)
    return str( 4 * (count / iterations))
    
print(MonteCarloUnitCircle(6000000))