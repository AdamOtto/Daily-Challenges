"""
You are given an array of length 24, where each element represents
the number of new subscribers during the corresponding hour.
Implement a data structure that efficiently supports the following:

update(hour: int, value: int): Increment the element at index hour by value.
query(start: int, end: int): Retrieve the number of subscribers that have
signed up between start and end (inclusive).
You can assume that all values get cleared at the end of
the day, and that you will not be asked for start and end values
that wrap around midnight.
"""
class Subsribers:
    d = None

    def __init__(self, Subs):
        if len(Subs) != 24 or type(Subs) != list:
            raise ValueError('Argument must be a list of size 24.')
        self.d = {}
        for i in range(24):
            self.d[i] = Subs[i]

    def update(self, hour, value):
        if hour < 1 or hour > 24:
            raise ValueError('Hour argument must be between 1 and 24.')
        if value < 0:
            raise ValueError('Value must be greater than or equal to 0.')
        self.d[hour - 1] = value

    def query(self, start, end):
        if (start < 1 or start > 24) or (end < 1 or end > 24):
            raise ValueError('Arguments must be greater than or equal to 0.')
        count = 0
        for i in range(start - 1, end):
            count += self.d[i]
        return count

in1 = [0,0,0,1,1,2,2,2,3,5,9,10,15,20,30,26,28,21,18,15,8,4,0,0]
Subs = Subsribers(in1)
# Return 6
print(Subs.query(1, 7))
Subs.update(1, 4)
# Return 10
print(Subs.query(1, 7))