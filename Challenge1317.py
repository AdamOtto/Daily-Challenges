"""
The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for
its order is an array representing whether each number is larger or smaller than the last.

Given this information, reconstruct an array that is consistent with it.
For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].
"""
def Solution(ar):
    l = len(ar)
    retVal = [0] * l
    
    lastMax = 0
    lastMin = 0
    
    for i in range(1, l):
        if  ar[i] == "+":
            retVal[i] = lastMax + 1
            lastMax += 1
        elif ar[i] == "-":
            retVal[i] = lastMin - 1
            lastMin -= 1
    
    for i in range(0, l):
        retVal[i] -= lastMin
    
    
    print(retVal)

    
# Return [2, 1, 3, 0, 4]
in1 = [None, "-", "+", "-", "+"]
Solution(in1)

# Return [6, 5, 4, 3, 7, 2, 1, 0, 8, 9]
in1 = [None, "-", "-", "-", "+", "-", "-", "-", "+", "+"]
Solution(in1)