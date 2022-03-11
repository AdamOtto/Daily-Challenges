"""
Implement a queue using a set of fixed-length arrays.

The queue should support enqueue, dequeue, and get_size operations.
"""

class Q:
    s = None
    w = None
    count = None
    x = None
    y = None
    q = None
    
    def __init__(self, width, size):
        self.s = size
        self.w = width
        self.q = [[None for i in range(0, width)] for j in range(size)]
        self.x = 0
        self.y = 0
    
    def enqueue(self, val):
        if self.x >= self.s or self.y >= self.w:
            print("Cannot add new element to queue.")
            return
        self.q[self.x][self.y] = val
        self.y += 1
        if self.y >= self.w:
            self.y = 0
            self.x += 1
        return
    
    def dequeue(self):
        if self.x == 0 and self.y == 0:
            return None
        temp = self.q[0][0]
        i = 0
        j = 1
        lasti = 0
        lastj = 0
        while i < self.s and j < self.w:
            if self.q[lasti][lastj] is None:
                break
            self.q[lasti][lastj] = self.q[i][j]
            lasti = i
            lastj = j
            
            j += 1
            if j >= self.w:
                j = 0
                i += 1
        self.q[lasti][lastj] = None
        
        self.y -= 1
        if self.y < 0:
            self.y = self.w - 1
            self.x -= 1
            if self.x < 0:
                self.x = 0
                self.y = 0
        return temp
    
    def get_size(self):
        return (self.x * self.w) + self.y

q = Q(2,3)

# Enqueue
print("Adding 1")
q.enqueue(1)
print("Adding 2")
q.enqueue(2)
print("Adding 3")
q.enqueue(3)
print("Adding 4")
q.enqueue(4)
print("Adding 5")
q.enqueue(5)
print("Adding 6")
q.enqueue(6)

# Cannot add element
print("Adding 7")
q.enqueue(7)

# Dequeue
print("Removing element (size:", q.get_size(), "): ", q.dequeue())
print("Removing element (size:", q.get_size(), "): ", q.dequeue())
print("Removing element (size:", q.get_size(), "): ", q.dequeue())
print("Removing element (size:", q.get_size(), "): ", q.dequeue())
print("Removing element (size:", q.get_size(), "): ", q.dequeue())
print("Removing element (size:", q.get_size(), "): ", q.dequeue())

# Remove from empty queue (return None)
print("Removing element (size:", q.get_size(), "): ", q.dequeue())
print("Removing element (size:", q.get_size(), "): ", q.dequeue())