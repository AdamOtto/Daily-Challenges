"""
Implement a queue using two stacks.
Recall that a queue is a FIFO (first-in, first-out)
data structure with the following methods:
enqueue, which inserts an element into the queue,
dequeue, which removes it.
"""

class twoStackQueue:
    s1 = None
    s2 = None
    
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, val):
        self.s1.append(val)
    
    def dequeue(self):
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop(-1))
        retVal = self.s2.pop(-1)
        while len(self.s2) > 0: 
            self.s1.append(self.s2.pop(-1))
        return retVal

test = twoStackQueue()
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
print(test.dequeue())
print(test.dequeue())
print(test.dequeue())