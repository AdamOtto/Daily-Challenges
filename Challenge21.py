"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""


# Solution 1.  Only works for base case.  Ran out of time.
def findClasses(times):
    #classes = []
    #classes[0] = times[0]
    classes = 1
    for i in range(1,len(times)):
        t1 = range(times[i][0], times[i][1] + 1)
        for j in range(0,i + 1):
            if i is not j:
                if not(times[j][0] in t1 or times[j][1] in t1):
                    classes -= 1
                    break
        classes += 1
    return str(classes)


in1 = [(30, 75), (0, 50), (60, 150)]
print(findClasses(in1))
