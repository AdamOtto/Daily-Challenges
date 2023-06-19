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

    
# Return [1, 2, 3, 0, 4]
in1 = [None, "+", "+", "-", "+"]
Solution(in1)

# Return [2, 1, 0]
in1 = [None, "-", "-"]
Solution(in1)

# Return [4, 3, 2, 1, 0]
in1 = [None, "-", "-", "-", "-"]
Solution(in1)

# Return [6, 5, 4, 7, 3, 8, 9, 10, 2, 11, 1, 0]
in1 = [None, "-", "-", "+", "-", "+", "+", "+", "-", "+", "-", "-"]
Solution(in1)

# Return [7, 6, 8, 5, 9, 4, 10, 3, 11, 2, 12, 1, 13, 0]
in1 = [None, "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"]
Solution(in1)