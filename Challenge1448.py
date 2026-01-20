"""
A wall consists of several rows of bricks of various integer lengths and uniform height.
Your goal is to find a vertical line going from the top to the bottom of the wall that cuts through the fewest number of bricks.
If the line goes through the edge between two bricks, this does not count as a cut.

For example, suppose the input is as follows, where values in each row represent the lengths of bricks in that row:

[[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]
The best we can we do here is to draw a line after the eighth brick,
which will only require cutting through the bricks in the third and fifth row.

Given an input consisting of brick lengths for each row such as the one above,
return the fewest number of bricks that must be cut to create a vertical line.
"""
def Solution(ar):
    l = len(ar)
    if l <= 1:
        if len(ar[0]) == 1:
            return 1
        return 0
    wl = sum(ar[0])
    retVal = l
    for i in range(1, wl):
        temp = 0
        for j in range(l):
            if not cleanCut(ar[j], i):
                temp += 1
        if temp < retVal:
            retVal = temp
    return retVal

def cleanCut(ar, cut):
    s = 0
    for i in range(len(ar)):
        s += ar[i]
        if s == cut:
            return True
        elif s > cut:
            return False
    return False

# Return 2
in1 = [[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]
print(Solution(in1))

# Return 1
print(Solution([[10]]))

# Return 0
print(Solution([[5,5]]))

# Return 2
in1 = [[6,4],
 [2, 8],
 [5, 5]]
print(Solution(in1))

# Return 3
in1 = [[10],
 [10],
 [10]]
print(Solution(in1))