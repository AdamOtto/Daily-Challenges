"""
Implement an LFU (Least Frequently Used) cache. It should be able to be
initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.

Got help from:
https://medium.com/@epicshane/a-python-implementation-of-lfu-least-frequently-used-cache-with-o-1-time-complexity-e16b34a3c49b
"""

class LFU:
    d = None
    cap = None
    freq_link_head = None
    def __init__(self, capacity):
        self.d = {}
        self.cap = capacity
        self.freq_link_head = None
    
    def get(self, key):
        if key in self.d:
            cache_node = self.d[key]
            freq_node = cache_node.freq_node
            value = cache_node.value
            
            self.move_forward(cache_node, freq_node)
            
            return value
        else:
            return -1
    
    def set(self, key, value):
        if self.cap <= 0:
            return -1
        
        if key not in self.d:
            if len(self.d) >= self.cap:
                self.dump_cache()
            self.create_cache(key, value)
        else:
            cache_node = self.d[key]
            freq_node = cache_node.freq_node
            value = freq_node.value
            self.move_forward(cache_node, freq_node)
    
    def move_forward(self, cache_node, freq_node):
        if freq_node.nxt is None or freq_node.nxt.freq != freq_node.freq + 1:
            target_freq_node = FreqNode(freq_node.freq + 1, None, None)
            target_empty = True
        else:
            target_freq_node = freq_node.nxt
            target_empty = False
        
        cache_node.free_myself()
        target_freq_node.append_cache_to_tail(cache_node)

        if target_empty:
            freq_node.insert_after_me(target_freq_node)


        if freq_node.count_caches() == 0:
            if self.freq_link_head == freq_node:
                self.freq_link_head = target_freq_node

            freq_node.remove()

    def dump_cache(self):
        head_freq_node = self.freq_link_head
        self.d.pop(head_freq_node.cache_head.key)
        head_freq_node.pop_head_cache()

        if head_freq_node.count_caches() == 0:
            self.freq_link_head = head_freq_node.nxt
            head_freq_node.remove()

    def create_cache(self, key, value):
        cache_node = CacheNode(key, value, None, None, None)
        self.d[key] = cache_node
        
        if self.freq_link_head is None or self.freq_link_head.freq != 0:
            new_freq_node = FreqNode(0, None, None)
            new_freq_node.append_cache_to_tail(cache_node)

            if self.freq_link_head is not None:
                self.freq_link_head.insert_before_me(new_freq_node)
            
            self.freq_link_head = new_freq_node
        else:
            self.freq_link_head.append_cache_to_tail(cache_node)
    
    
class CacheNode:
    key = None
    value = None
    freq_node = None
    pre = None
    nxt = None
    def __init__(self, key, value, freq_node, pre, nxt):
        self.key = key
        self.value = value
        self.freq_node = freq_node
        self.pre = pre
        self.nxt = nxt
    
    def free_myself(self):
        if self.freq_node.cache_head == self.freq_node.cache_tail:
            self.freq_node.cache_head = self.freq_node.cache_tail = None
        elif self.freq_node.cache_head == self:
            self.nxt.pre = None
            self.freq_node.cache_head = self.nxt
        elif self.freq_node.cache_tail == self:
            self.pre.nxt = None
            self.freq_node.cache_tail = self.pre
        else:
            self.pre.nxt = self.nxt
            self.nxt.pre = self.pre

        self.pre = None
        self.nxt = None
        self.freq_node = None

class FreqNode(object):
    """
    doubly linked list
    """
    def __init__(self, freq, pre, nxt):
        self.freq = freq
        self.pre = pre # previous FreqNode
        self.nxt = nxt # next FreqNode
        self.cache_head = None # CacheNode head under this FreqNode
        self.cache_tail = None # CacheNode tail under this FreqNode

    def count_caches(self):
        if self.cache_head is None and self.cache_tail is None:
            return 0
        elif self.cache_head == self.cache_tail:
            return 1
        else:
            return '2+'

    def remove(self):
        if self.pre is not None:
            self.pre.nxt = self.nxt
        if self.nxt is not None:
            self.nxt.pre = self.pre

        pre = self.pre
        nxt = self.nxt
        self.pre = self.nxt = self.cache_head = self.cache_tail = None

        return (pre, nxt)

    def pop_head_cache(self):
        if self.cache_head is None and self.cache_tail is None:
            return None
        elif self.cache_head == self.cache_tail:
            cache_head = self.cache_head
            self.cache_head = self.cache_tail = None
            return cache_head
        else:
            cache_head = self.cache_head
            self.cache_head.nxt.pre = None
            self.cache_head = self.cache_head.nxt
            return cache_head

    def append_cache_to_tail(self, cache_node):
        cache_node.freq_node = self

        if self.cache_head is None and self.cache_tail is None:
            self.cache_head = self.cache_tail = cache_node
        else:
            cache_node.pre = self.cache_tail
            cache_node.nxt = None
            self.cache_tail.nxt = cache_node
            self.cache_tail = cache_node

    def insert_after_me(self, freq_node):
        freq_node.pre = self
        freq_node.nxt = self.nxt

        if self.nxt is not None:
            self.nxt.pre = freq_node
        
        self.nxt = freq_node

    def insert_before_me(self, freq_node):
        if self.pre is not None:
            self.pre.nxt = freq_node
        
        freq_node.pre = self.pre
        freq_node.nxt = self
        self.pre = freq_node

# Return 1, 2, 3
in1 = LFU(3)
in1.set(1,1)
in1.set(2,2)
in1.set(3,3)
print(in1.get(1))
print(in1.get(2))
print(in1.get(3))

print()

# Print 1,2,-1,4
in1.get(1)
in1.get(2)
in1.set(4,4)
print(in1.get(1))
print(in1.get(2))
print(in1.get(3))
print(in1.get(4))