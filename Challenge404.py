"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

def Solution(ar):
    if len(ar) == 0:
        return []
    retVal = []
    retVal.append( [ar[0]] )
    
    for i in range(1, len(ar)):
        newRoom = True
        for j in range(0, len(retVal)):
            if not lectureInTimes(retVal[j], ar[i]):
                retVal[j].append(ar[i])
                newRoom = False
                break
        if newRoom:
            retVal.append([ar[i]])
    return len(retVal)

def lectureInTimes(times, lecture):
    for t in times:
        if lecture[0] in range(t[0], t[1] + 1) or lecture[1] in range(t[0], t[1] + 1):
            return True
    return False

# Return 2
print(Solution([(30, 75), (0, 50), (60, 150)]))

# Return 1
print(Solution([(1,3), (6,9), (4,5)]))

# Return 2
print(Solution([(1,3), (6,9), (4,5), (1,9)]))