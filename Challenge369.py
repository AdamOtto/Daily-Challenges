"""
You’re tracking stock price at a given instance of time.
Implement an API with the following functions: add(), update(), remove(),
which adds/updates/removes a datapoint for the stock price you are tracking.
The data is given as (timestamp, price), where timestamp is specified in unix epoch time.

Also, provide max(), min(), and average() functions that give the
max/min/average of all values seen thus far.
"""

class StockAPI:
    d = None
    def __init__(self):
        self.d = {}
    
    def add(self, time, price):
        if time not in self.d:
            self.d[time] = 0
        self.d[time] = price
    
    def update(self, time, price):
        if time in self.d:
            self.d[time] = price
    
    def remove(self, time):
        if time in self.d:
            del self.d[time]
    
    def max(self):
        retVal = 0
        for key, val in self.d.items():
            retVal = max(retVal, val)
        return retVal
    
    def min(self):
        retVal = None
        for key, val in self.d.items():
            if retVal is None:
                retVal = val
            else:
                retVal = min(retVal, val)
        return retVal
        
    def average(self):
        retVal = 0
        for key, val in self.d.items():
            retVal += val
        return retVal / len(self.d)


in1 = StockAPI()
in1.add(1232313, 100)
in1.add(1232449, 139)
in1.add(1233205, 134)
in1.add(1233924, 140)
in1.add(1234071, 144)

in1.update(1233924, 138)

in1.remove(1234071)

# Return 139, 100, 127.75, respectively.
print(in1.max())
print(in1.min())
print(in1.average())