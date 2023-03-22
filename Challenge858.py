"""
Compute the running median of a sequence of numbers.
That is, given a stream of numbers, print out the median
of the list so far on each new element.

Recall that the median of an even-numbered
list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""
import math
def Solution(ar):
    retVal = []
    l = len(ar)
    for i in range(l):
        retVal.append(FindMedian(sorted(ar[0:i + 1])))
    return retVal

def FindMedian(ar):
    l = len(ar)
    if l % 2 >= 1:
        if l == 1:
            return ar[0]
        else:
            return ar[int(math.floor(l / 2))]
    else:
        return (ar[int(l / 2)] + ar[int(l / 2) - 1]) / 2
        
# Return [2, 1.5, 2, 3.5, 2, 2.0, 2]
print(Solution([2, 1, 5, 7, 2, 0, 5]))

# Return [43, 28.5, 25, 34.0, 32, 37.5]
print(Solution([43,14,25,65,32,59]))