"""
On a mysterious island there are creatures known as Quxes
which come in three colors: red, green, and blue.
One power of the Qux is that if two of them are standing next to each other,
they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining
after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'],
it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
"""
import sys

def Solution(Qux):
    l = len(Qux)
    if l == 1:
        return 1
    retVal = l
    
    for i in range(1, l):
        temp = combineQux(Qux, i - 1, i)
        if len(temp) < l:
            retVal = min(Solution(temp), retVal)
    return retVal

def combineQux(ls, Qux1, Qux2):
    l = len(ls)
    t = ''
    if (ls[Qux1] == 'R' or ls[Qux2] == 'R') and (ls[Qux1] == 'G' or ls[Qux2] == 'G'):
        t = 'B'
    elif (ls[Qux1] == 'R' or ls[Qux2] == 'R') and (ls[Qux1] == 'B' or ls[Qux2] == 'B'):
        t = 'G'
    elif  (ls[Qux1] == 'G' or ls[Qux2] == 'G') and (ls[Qux1] == 'B' or ls[Qux2] == 'B'):
        t = 'R'
    
    if t != '':
        retVal = []
        retVal.extend(ls[0:Qux1])
        retVal.append(t)
        retVal.extend(ls[Qux2 + 1:l])
        return retVal
    else:
        return ls

# Returns 1.
in1 = ['R', 'G', 'B', 'G', 'B']
print(Solution(in1))

# Returns 5. 
in1 = ['R', 'R', 'R', 'R', 'R']
print(Solution(in1))

# Returns 2, smallest is [B, B] or [G, G]
in1 = ['R', 'R', 'B', 'R', 'G']
print(Solution(in1))