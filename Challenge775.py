"""
Given an array of time intervals (start, end) for classroom
lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
def Solution(ar):
    l = len(ar)
    if l == 0:
        return None
    if l == 1:
        return 1
    temp = sorted(ar, key=lambda tup: tup[0])
    classrooms = []
    classrooms.append([temp[0]])
    for i in range(1, l):
        noClassroomFound = True
        for j in range(len(classrooms)):
            if temp[i][0] >= classrooms[j][-1][1]:
                noClassroomFound = False
                classrooms[j].append(temp[i])
                break
        if noClassroomFound:
            classrooms.append([temp[i]])
    
    return len(classrooms)

# Return 2
print(Solution([(30, 75), (0, 50), (60, 150)]))
# Return 3
print(Solution([(0, 4), (1, 3), (3, 6), (4, 8), (2, 5), (5, 6)]))
# Return 1
print(Solution([(4, 6), (1, 3), (0, 1), (3, 4)]))