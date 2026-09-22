"""
Implement a stack using only a heap.
A stack implements the following methods:

    push(item), which adds an element to the stack
    pop(), which removes and returns the most recently added element
    (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:
    push(item), which adds a new key to the heap
    pop(), which removes and returns the min value of the heap
"""
import heapq
import sys

class heapStack:
    h = None
    count = None
    def __init__(self):
        self.h = []
        heapq.heapify(self.h)
        self.count = sys.maxsize
    
    def push(self, item):
        heapq.heappush(self.h, (self.count, item))
        self.count -= 1
    
    def pop(self):
        self.count += 1
        temp = heapq.heappop(self.h)
        return temp[1]

temp = heapStack()
temp.push(1)
temp.push(2)
temp.push(3)
# Return 3, 2, 1
print(temp.pop())
print(temp.pop())
print(temp.pop())