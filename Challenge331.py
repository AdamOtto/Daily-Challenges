"""
You are given a string consisting of the letters x and y, such as xyxxxyxyy.
In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come
before all y's. In the preceding example, it suffices to flip the second and sixth characters,
so you should return 2.
"""

# Brute force approach
def Solution1(ar):
    l = len(ar)
    temp1 = []
    for i in range(l):
        temp1.append("y")
    temp2 = list(ar)
    retVal = compare(l, temp1, temp2)
    
    for i in range(l):
        temp1[i] = 'x'
        retVal = min(retVal, compare(l, temp1, temp2))
    return retVal

def compare(l, ar1, ar2):
    retVal = 0
    for i in range(l):
        if ar1[i] != ar2[i]:
            retVal += 1
    return retVal

# More methodical approach
def Solution2(ar):
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
in1 = "xyxxxyxyy"
print(Solution1(in1))
print(Solution2(in1))

# Return 3
in1 = "xyxyxyx"
print(Solution1(in1))
print(Solution2(in1))

# Return 0
in1 = "xxxxxxxxxx"
print(Solution1(in1))
print(Solution2(in1))

# Return 3
in1 = "yyyxxx"
print(Solution1(in1))
print(Solution2(in1))