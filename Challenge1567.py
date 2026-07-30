"""
You are given a list of data entries that represent entries and exits of groups
of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building.
Return it as a pair of (start, end) timestamps.
You can assume the building always starts off and ends up empty, i.e. with 0 people inside.
"""
class TimeEntry:

    timestamp = None
    count = None
    type = None

    def __init__(self, time, peopleCount, EnterOrExit):
        self.timestamp = time
        self.count = peopleCount
        self.type = EnterOrExit

class TimeLog:

    log = None
    length = 0

    def __init__(self):
        self.log = []
        self.length = 0

    def addTime(self, Entry):

        if self.length == 0:
            self.log.append(Entry)
            self.length += 1
            return

        if Entry.timestamp < self.log[0].timestamp:
            self.log.insert(0, Entry)
            self.length += 1
            return

        for i in range(1, self.length - 1):
            if Entry.timestamp <= self.log[i + 1].timestamp and Entry.timestamp > self.log[i - 1].timestamp:
                self.log.insert(i, Entry)
                self.length += 1
                return

        self.log.append(Entry)
        self.length += 1
        return


def Solution(in1):
    count = 0
    highCount = 0
    start = 0
    end = 0

    for i in range(0, in1.length):
        if in1.log[i].type == "enter":
            count += in1.log[i].count
        elif in1.log[i].type == "exit":
            count -= in1.log[i].count

        if count > highCount:
            highCount = count
            start = in1.log[i].timestamp
            end = in1.log[i+1].timestamp


    return (start, end)


in1 = TimeLog()
in1.addTime( TimeEntry(1060, 3, "enter") )
in1.addTime( TimeEntry(1080, 5, "exit") )
in1.addTime( TimeEntry(1000, 3, "enter") )
in1.addTime( TimeEntry(1040, 2, "exit") )
in1.addTime( TimeEntry(1020, 1, "enter") )
# Return (1060, 1080)
print(Solution(in1))