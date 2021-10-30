"""
A quack is a data structure combining properties of both stacks and queues.
It can be viewed as a list of elements written left to right such that three operations are possible:

push(x): add a new item x to the left end of the list
pop(): remove and return the item on the left end of the list
pull(): remove the item on the right end of the list.

Implement a quack using three stacks and O(1) additional memory, so that the amortized time for any push, pop, or pull operation is O(1).
"""

class quack:
    
    q1 = None
    q2 = None
    q3 = None
    start = None
    end = None
    l = None
    def __init__(self, size):
        self.s = size
        self.l = int(size / 3)
        self.q1 = [None] * self.l
        self.q2 = [None] * self.l
        self.q3 = [None] * int(size - (2 * self.l))
        self.start = [1, int((size / 3) / 2)]
        self.end = [1, int((size / 3) / 2) + 1]
        if self.end[1] >= self.l:
            self.end[1] = self.l - 1

    def push(self, x):
        
        if self.start[0] == 0 and self.start[1] == 0:
            if self.q1[0] == None:
                self.q1[0] = x
            else:
                temp = self.q1.pop(-1)
                self.q1.insert(0, x)
                self.q2.insert(0, temp)
                temp = self.q2.pop(-1)
                self.q3.insert(0, temp)
                self.q3.pop(-1)
                
                self.end[1] += 1
                if self.end[1] >= self.l:
                    self.end[1] = 0
                    self.end[0] += 1
                    if self.end[0] > 2:
                        self.end[0] = 2
                        self.end[1] = len(q2) - 1
        else:
            if self.start[0] == 0:
                self.q1[self.start[1]] = x
            elif self.start[0] == 1:
                self.q2[self.start[1]] = x
            elif self.start[0] == 2:
                self.q3[self.start[1]] = x
            
            self.start[1] -= 1
            
            if self.start[1] < 0:
                self.start[0] -= 1
                if self.start[0] == 0:
                    self.start[1] = len(self.q1) - 1
                elif self.start[0] == 1:
                    self.start[1] = len(self.q2) - 1
                elif self.start[0] == 2:
                    self.start[1] = len(self.q3) - 1
    
    def pop(self):
        retVal = None
        if self.start[0] == 0:
            retVal = self.q1[self.start[1]]
            self.q1[self.start[1]] = None
        elif self.start[0] == 1:
            retVal = self.q2[self.start[1]]
            self.q2[self.start[1]] = None
        elif self.start[0] == 2:
            retVal = self.q3[self.start[1]]
            self.q3[self.start[1]] = None
        
        self.start[1] += 1
        if self.start[0] != 2:
            if self.start[1] >= self.l:
                self.start[1] = 0
                self.start[0] += 1
        else:
            if self.start[1] >= len(self.q3):
                self.start[1] = len(self.q3) - 1
        if self.start[0] >= self.end[0] and self.start[1] >= self.end[1]:
            self.end[0] = self.start[0]
            self.end[1] = self.start[1]
        return retVal
    
    def pull(self):
        retVal = None

        if self.end[0] == 0:
            retVal = self.q1[self.end[1]]
            self.q1[self.end[1]] = None
        elif self.end[0] == 1:
            retVal = self.q2[self.end[1]]
            self.q2[self.end[1]] = None
        elif self.end[0] == 2:
            retVal = self.q3[self.end[1]]
            self.q3[self.end[1]] = None
            
        self.end[1] -= 1
        if self.end[1] < 0:
            self.end[0] -= 1
            if self.end[0] < 0:
                self.end[0] = 0
                self.end[1] = 0
            else:
                self.end[1] = self.l
        return retVal
    
    def display(self):
        temp = []
        temp.extend(self.q1)
        temp.extend(self.q2)
        temp.extend(self.q3)
        print(temp)
    
q = quack(3)
q.push(3)
# Return [None, 3, None]
q.display()
q.push(2)
q.push(1)
# Return [1,2,3]
q.display()

# Return [1,2,None]
q.pull()
q.display()

# Return [None, 2, None]
q.pop()
q.display()