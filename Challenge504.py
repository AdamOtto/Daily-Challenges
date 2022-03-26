"""
You run an e-commerce website and want to
record the last N order ids in a log.

Implement a data structure to accomplish this,
with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

class logs:
    
    l = None
    
    def __init__(self):
        self.l = []
    
    def record(self, order_id):
        self.l.append(order_id)
    
    def get_last(self, i):
        if i < 0:
            return None
        N = len(self.l)
        return self.l[N - i - 1]

in1 = logs()
for i in range(1, 101):
    in1.record(i)

# Return 100
print(in1.get_last(0))

# Return 50
print(in1.get_last(50))