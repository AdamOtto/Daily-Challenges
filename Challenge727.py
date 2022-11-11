"""
Compute the running median of a sequence of numbers.
That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

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
    medLow = medHigh = 0
    l = len(ar)
    retVal = []
    if l == 0:
        return
    if l >= 1:
        retVal.append("{:.1f}".format(ar[0]))
    if l >= 2:
        retVal.append( "{:.1f}".format((ar[0] + ar[1]) / 2))
    else:
        return retVal
    
    for i in range(2, l):
        temp = sorted(ar[0:i + 1])
        if (i + 1) % 2 == 1:
            retVal.append("{:.1f}".format(temp[math.floor(len(temp) / 2)]))
        else:
            retVal.append("{:.1f}".format((temp[int(len(temp) / 2)] + temp[ (int(len(temp) / 2)) - 1]) / 2))
    return retVal
    
# Return ['2.0', '1.5', '2.0', '3.5', '2.0', '2.0', '2.0']
print(Solution([2, 1, 5, 7, 2, 0, 5]))

# Return ['5.0', '7.5']
print(Solution([5,10]))

# Return ['1.0']
print(Solution([1]))