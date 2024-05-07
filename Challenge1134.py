"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers,
print out the median of the list so far on each new element.

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
    sm = []
    for i in range(len(ar)):
        sm.append(ar[i])
        sm.sort()
        if len(sm) % 2 == 1:
            print(sm[math.floor(len(sm) / 2)])
        else:
            print((sm[int(len(sm) / 2)] + sm[int((len(sm) / 2)) - 1]) / 2)
    return


# Return 2, 1.5, 2, 3.5, 2, 2.0, 2
Solution([2, 1, 5, 7, 2, 0, 5])