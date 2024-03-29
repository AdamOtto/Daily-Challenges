"""
Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

set(key, value, time): sets key to value for t = time.
get(key, time): gets the key at t = time.
The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2
d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
"""
class keyTime:
    
    d = {}

    def setVal(self,key, value, time):
        
        if key not in self.d:
            self.d[key] = []
            self.d[key].append( (value,time) )
        else:
            temp = self.d[key]
            i = 0
            for val,t in temp:
                if time == t:
                    self.d[key][i] = (value, time)
                    return
                i += 1
            self.d[key].append( (value, time) )
                
                
    def get(self,key, time):
        temp = self.d[key]
        retVal = None
        for val,t in temp:
            if t <= time:
                retVal = val
        return retVal
                
                
d = keyTime()

d.setVal(1, 1, 0) # set key 1 to value 1 at time 0
d.setVal(1, 2, 2) # set key 1 to value 2 at time 2
print(d.get(1, 1)) # get key 1 at time 1 should be 1
print(d.get(1, 3)) # get key 1 at time 3 should be 2
d.setVal(1, 1, 5) # set key 1 to value 1 at time 5
print(d.get(1, 0)) # get key 1 at time 0 should be null
print(d.get(1, 10)) # get key 1 at time 10 should be 1
d.setVal(1, 1, 0) # set key 1 to value 1 at time 0
d.setVal(1, 2, 0) # set key 1 to value 2 at time 0
print(d.get(1, 0)) # get key 1 at time 0 should be 2