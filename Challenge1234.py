"""
On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue.
One power of the Qux is that if two of them are standing next to each other,
they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them
remaining after any possible sequence of such transformations.

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
def Solution(ar):
    retVal = len(ar)
    for i in range(1, len(ar)):
        if ar[i - 1] != ar[i]:
            retVal = min(retVal, Solution(ar[:i-1] + list(NewQuxes(ar[i - 1], ar[i])) + ar[i + 1:]))
    return retVal
    
def NewQuxes(ar1, ar2):
    if ar1 == 'R':
        if ar2 == 'G':
            return 'B'
        elif ar2 == 'B':
            return 'G'
    if ar1 == 'G':
        if ar2 == 'R':
            return 'B'
        elif ar2 == 'B':
            return 'R'
    if ar1 == 'B':
        if ar2 == 'G':
            return 'R'
        elif ar2 == 'R':
            return 'G'
# Return 1
print(Solution(['R', 'G', 'B', 'G', 'B']))

# Return 3
print(Solution(['R', 'R', 'R']))