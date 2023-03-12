"""
Implement an LRU (Least Recently Used) cache.
It should be able to be initialized with a cache size n,
and contain the following methods:
set(key, value): sets key to value. If there are already n items in the cache
and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
"""
from collections import OrderedDict

class LRU:
    d = None
    l = None
    def __init__(self, n):
        self.d = OrderedDict()
        self.l = n
    def set(self, key, value):
        self.d[key] = value
        self.d.move_to_end(key)
        if len(self.d) > self.l:
            self.d.popitem(last = False)
        
    
    def get(self, key):
        if key in self.d:
            return self.d[key]
        return None

c = LRU(2)

# Return 1\n2
c.set(1, 1)
c.set(2, 2)
print(c.get(1))
print(c.get(2))

print()
# Return None\n2\n3
c.set(3, 3)
print(c.get(1))
print(c.get(2))
print(c.get(3))