"""
Given a list of integers, return the largest product
that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2],
we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""

def Solution(ar):
    if len(ar) < 3:
        return False
    elif len(ar) == 3:
        return ar[0] * ar[1] * ar[2]
    negatives = []
    positives = []
    for a in ar:
        if a < 0:
            negatives.append(a)
        elif a > 0:
            positives.append(a)
    
    negatives = sorted(negatives)
    positives = sorted(positives, reverse = True)
    
    if len(negatives) >= 2 and len(positives) >= 3:
        return max( negatives[0] * negatives[1] * positives[0],  positives[0] * positives[1] * positives[2])
    elif len(negatives) >= 2 and len(positives) <= 2 and len(positives) != 0:
        return negatives[0] * negatives[1] * positives[0]
    elif len(positives) == 0:
        return negatives[-1] * negatives[-2] * negatives[-3]
    return None

# Return 500
print(Solution([-10, -10, 5, 2]))

# Return -100
print(Solution([-10, -10, -5, -2]))

# Return 60
print(Solution([-2, -3, -4, 5]))

# Return 60
print(Solution([1, -2, -3, -4, 5]))

# Return -10
print(Solution([1, -2, 5]))