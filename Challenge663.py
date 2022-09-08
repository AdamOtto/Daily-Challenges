"""
Design and implement a HitCounter class that keeps track of requests (or hits).
It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
Follow-up: What if our system has limited memory?
"""
from datetime import datetime


class HitCounter:
    hits = None
    def __init__(self):
        self.hits = []
    
    def record(self, timestamp):
        temp = self.find(timestamp)
        if temp != -1:
            #print("inserting", timestamp, "into index", temp, "for", self.hits)
            self.hits.insert(temp, timestamp)
        else:
            return False
        return True
      
    def find(self, time):
        if len(self.hits) == 0:
            return 0
        if len(self.hits) == 1:
            if time >= self.hits[0]:
                return 1
            return 0
        
        high = len(self.hits) - 1
        low = 0
        mid = int((high - low) / 2) + low
        
        if time <= self.hits[low]:
            return low
        if time >= self.hits[high]:
            return high + 1
        
        while low < mid and mid < high:
            if self.hits[mid - 1] <= time and time <= self.hits[mid]:
                return mid
            elif self.hits[mid] < time:
                low = mid
            elif self.hits[mid] > time:
                high = mid
            mid = int((high - low) / 2) + low
        return -1
    
    def total(self):
        return len(self.hits)
    
    def range(self, lower, upper):
        temp1 = self.find(lower)
        temp2 = self.find(upper)
        if upper < self.hits[temp2]:
            return len(self.hits[temp1: temp2])
        return len(self.hits[temp1: temp2 + 1])
        
"""
curr_dt = datetime.now()
HC = HitCounter()
print(HC.record(int(round(curr_dt.timestamp()))))
print(HC.total())
"""

HC = HitCounter()
HC.record(64445018)
HC.record(64445027)
HC.record(64445035)
HC.record(64445023)
HC.record(64445022)
HC.record(64445021)
# Return 6
print(HC.total())
# Return 3
print(HC.range(64445019, 64445025))
# Return [64445018, 64445021, 64445022, 64445023, 64445027, 64445035]
print(HC.hits)