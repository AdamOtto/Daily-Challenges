"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
def Solution(ar):
    temp = sorted(ar, key=lambda x: x[0])
    l = len(ar)
    retVal = 0
    for i in range(1, l):
        if temp[i - 1][1] > temp[i][0]:
            retVal += 1
    return retVal

# Return 2
print(Solution([(30, 75), (0, 50), (60, 150)]))

# Return 3
print(Solution([(0, 15), (10, 25), (15, 30), (25,40)]))