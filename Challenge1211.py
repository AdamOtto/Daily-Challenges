"""
Given a stack of N elements, interleave the first half of the stack
with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack,
and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3].
If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
"""
import math

class Stack:
    data = []
    def __init__(self, initData):
        self.data = initData
    def push(self, element):
        self.data.insert(0, element)
    def pop(self):
        return self.data.pop(0)
    def length(self):
        return len(self.data)

class Queue:
    data = []
    def __init__(self, initData):
        self.data = initData
    def enqueu(self, element):
        self.data.append(element)
    def dequeue(self):
        return self.data.pop(0)

def Solution(stack, queue):
    N = stack.length()
    topN = math.ceil(N/2)
    bottomN = N - topN

    #Push everything into queue
    for i in range(0, N):
        queue.enqueu(stack.pop())

    #Push the top half into the stack, reversing it.
    for i in range(0, topN):
        stack.push(queue.dequeue())

    # Interleave the bottom and top half of the stack
    queueSwitch = False
    if N % 2 == 0:
        queueSwitch = True
    for i in range(0, N):
        if queueSwitch:
            queue.enqueu(queue.dequeue())
            queueSwitch = False
        else:
            queue.enqueu(stack.pop())
            queueSwitch = True

    # Push everything back into stack
    for i in range(0, N):
        stack.push(queue.dequeue())

    return

# Return [1, 5, 2, 4, 3]
stack = Stack([1,2,3,4,5])
queue = Queue([])
Solution(stack, queue)
print(stack.data)

# Return [1, 4, 2, 3]
stack = Stack([1,2,3,4])
queue = Queue([])
Solution(stack, queue)
print(stack.data)

# Return [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
stack = Stack([10,12,14,16,18,20,19,17,15,13,11])
queue = Queue([])
Solution(stack, queue)
print(stack.data)