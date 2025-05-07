"""
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
class OrderLog:
    log = None
    N = None
    def __init__(self, N):
        self.log = []
        self.N = N
    
    def record(self, newOrder):
        self.log.append(newOrder)
        if len(self.log) > self.N:
            self.log.pop(0)
    
    def get_last(self, i):
        if i <= self.N:
            return self.log[self.N - i]
        return None

# Return 3,2,1,None      
orders = OrderLog(3)
orders.record(1)
orders.record(2)
orders.record(3)
print(orders.get_last(1))
print(orders.get_last(2))
print(orders.get_last(3))
print(orders.get_last(4))

print()

# Return 51
orders = OrderLog(100)
for i in range(1, 101):
    orders.record(i)
print(orders.get_last(50))