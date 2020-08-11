'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''


def findRooms(times):
    classroom = []
    classroom.append([times[0]])

    for i in range(1, len(times)):
        newClassAdded = False
        for j in classroom:
            if not RoomOccupied(times[i], j):
                j.append(times[i])
                newClassAdded = True
                break
        if not newClassAdded:
            classroom.append([times[i]])
    print(len(classroom))
    #print(classroom)

def RoomOccupied(time, room):
    tr = range(time[0], time[1] + 1)
    for i in room:
        if i[0] in tr or i[1] in tr:
            return True
    return False


in1 = [(30, 75), (0, 50), (0, 29), (60, 150)]
findRooms(in1)