"""
Create a data structure that performs all the following operations in O(1) time:

plus: Add a key with value 1. If the key already exists, increment its value by one.

minus: Decrement the value of a key. If the key's value is currently 1, remove it.

get_max: Return a key with the highest value.

get_min: Return a key with the lowest value.
"""
class adder:
    dkey = None
    dval = None
    maxVal = None
    minVal = None
    lastMinVal = None
    
    def __init__(self):
        self.dkey = {}
        self.dval = {}
        self.maxVal = 0
        self.minVal = 1
        self.lastMinVal = []
        
    
    def plus(self, val):
        new = False
        # Update dkey
        if val not in self.dkey:
            self.dkey[val] = 1
            new = True
        else:
            self.dkey[val] += 1
        
        # Update dval
        if self.dkey[val] not in self.dval:
            self.dval[self.dkey[val]] = []
            self.dval[self.dkey[val]].append(val)
        else:
            self.dval[self.dkey[val]].append(val)
        
        if not new:
            self.dval[self.dkey[val] - 1].remove(val)
        else:
            self.lastMinVal.append(self.minVal)
            self.minVal = self.dkey[val]
            
        if self.dkey[val] > self.maxVal:
            self.maxVal = self.dkey[val]
        if len(self.dval[self.minVal]) == 0 and not new:
            self.lastMinVal.append(self.minVal)
            self.minVal += 1
    
    def minus(self, val):
        # Update dkey
        if val not in self.dkey:
            return
        
        if self.dkey[val] == 1:
            del self.dkey[val]
            self.minVal = self.lastMinVal.pop()
            self.dval[1].remove(val)
        else:
            if self.dkey[val] == self.maxVal:
                self.maxVal -= 1
            if self.dkey[val] == self.minVal:
                self.minVal -= 1
            
            self.dval[self.dkey[val]].remove(val)
            
            self.dkey[val] -= 1
            self.dval[self.dkey[val] ].append(val)
    
    def get_max(self):
        if len(self.dval[self.maxVal]) > 0:
            return self.dval[self.maxVal][0]
        else:
            return None
    
    def get_min(self):
        if len(self.dval[self.minVal]) > 0:
            return self.dval[self.minVal][0]
        else:
            return None

d = adder()

# get_min and get_max should return 1
d.plus(1)
print(d.get_max())
print(d.get_min())

# get_min should return 2 and get_max should return 1
d.plus(1)
d.plus(2)
d.plus(3)
d.plus(3)
print(d.get_max())
print(d.get_min())

# get_min and get_max should return 1 or 3
d.minus(1)
d.minus(2)
d.minus(3)
print(d.get_max())
print(d.get_min())

# get_min and get_max should return None
d.minus(1)
d.minus(3)
print(d.get_max())
print(d.get_min())