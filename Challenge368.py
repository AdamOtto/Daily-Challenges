"""
Implement a key value store, where keys and values are integers, with the following methods:

update(key, vl): updates the value at key to val, or sets it if doesn't exist
get(key): returns the value with key, or None if no such value exists
max_key(val): returns the largest key with value val, or None if no key with that value exists
For example, if we ran the following calls:

kv.update(1, 1)
kv.update(2, 1)
And then called kv.max_key(1), it should return 2, since it's the largest key with value 1
"""

class keyStore:
    
    dk = None
    dv = None
    
    def __init__(self):
        self.dk = {}
        self.dv = {}
    
    def update(self, key, value):
        oldVal = None
        if key not in self.dk:
            oldVal = value
            self.dk[key] = value
        else:
            oldVal = self.dk[key]
            self.dk[key] = value
        
        if oldVal in self.dv:
            if key in self.dv[oldVal]:
                self.dv[oldVal].remove(key)
        
        if value not in self.dv:
            self.dv[value] = []
        self.dv[value].append(key)
            
    
    def max_key(self, value):
        if value in self.dv:
            return max(self.dv[value])
        return None
    
    def get(self, key):
        if key in self.dk:
            return self.dk[key]
        return None

kv = keyStore()
kv.update(1, 1)
kv.update(2, 1)
# Return 2
print(kv.max_key(1))
kv.update(2, 2)
# Return 1
print(kv.max_key(1))
# Return 2
print(kv.max_key(2))