"""
You are given a string consisting of the letters x and y, such as xyxxxyxyy.
In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come
before all y's. In the preceding example, it suffices to flip the second and sixth characters,
so you should return 2.
"""

def Solution(ar):
    l = len(ar)
    rightY = [0]*l
    if ar[0] == 'y':
        rightY[0] = 1
    leftX = [0]*l
    if ar[l - 1] == 'x':
        leftX[l-1] = 1
    
    for i in range(1, l):
        if ar[i] == "y":
            rightY[i] += 1
        rightY[i] += rightY[i - 1]
    for i in reversed(range(l - 1)):
        if ar[i] == "x":
            leftX[i] += 1
        leftX[i] += leftX[i + 1]
    retVal = l
    for i in range(0, l):
        retVal = min(retVal, leftX[i] + rightY[i])
    return retVal - 1

# Return 2
print(Solution("xyxxxyxyy"))

# Return 3
print(Solution("xyxyxyx"))

# Return 0
print(Solution("yyy"))

# Return 3
print(Solution("yyyxxx"))