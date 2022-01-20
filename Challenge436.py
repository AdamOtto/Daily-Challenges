"""
Implement 3 stacks using a single list
"""

class Stack:
    l = None
    i1 = None
    i2 = None
    
    def __init__(self):
        self.l = []
        self.i1 = 0
        self.i2 = 0

    def pop(self, stack_number):
        if stack_number < 1 or stack_number > 3:
            return None
        retVal = None
        if stack_number == 1:
            if self.i1 > 0:
                self.i1 -= 1
                self.i2 -= 1
                retVal = self.l.pop(self.i1)
        if stack_number == 2:
            if self.i2 > 0 and self.i2 > self.i1:
                self.i2 -= 1
                retVal = self.l.pop(self.i2)
        if stack_number == 3:
            if len(self.l) > self.i2:
                retVal = self.l.pop(-1)
        
        return retVal

    def push(self, item, stack_number):
        
        if stack_number < 1 or stack_number > 3:
            return None
        
        if stack_number == 1:
            self.l.insert(self.i1, item)
            self.i1 += 1
            self.i2 += 1
        elif stack_number == 2:
            self.l.insert(self.i2, item)
            self.i2 += 1
                
        elif stack_number == 3:
            self.l.append(item)


in1 = Stack()

in1.push(1,1)
print("Current stack: ", str(in1.l))
in1.push(1,2)
print("Current stack: ", str(in1.l))
in1.push(1,3)
print("Current stack: ", str(in1.l))
in1.push(2,1)
print("Current stack: ", str(in1.l))
in1.push(2,2)
print("Current stack: ", str(in1.l))
in1.push(2,3)
print("Current stack: ", str(in1.l))
in1.push(3,1)
print("Current stack: ", str(in1.l))
in1.push(3,2)
print("Current stack: ", str(in1.l))
in1.push(3,3)
print("Current stack: ", str(in1.l))

print()

print("Popping stack 1 5 times")
in1.pop(1)
in1.pop(1)
in1.pop(1)
in1.pop(1)
print("Current stack: ", str(in1.l))

print()

print("Popping stack 2 and 3 once")
in1.pop(2)
in1.pop(3)
print("Current stack: ", str(in1.l))

print()

print("Repopulating stack 1 with [1,2,3]")
in1.push(1,1)
in1.push(2,1)
in1.push(3,1)
print("Current stack: ", str(in1.l))

print()

print("Popping stack 2 4 times")
in1.pop(2)
in1.pop(2)
in1.pop(2)
in1.pop(2)
print("Current stack: ", str(in1.l))

print()

print("Popping stack 3 4 times")
in1.pop(3)
in1.pop(3)
in1.pop(3)
in1.pop(3)
print("Current stack: ", str(in1.l))

print()

print("Popping stack 1 4 times")
in1.pop(1)
in1.pop(1)
in1.pop(1)
in1.pop(1)
print("Current stack: ", str(in1.l))

print()

print("pushing 1 into each stack")
in1.push(1,1)
in1.push(1,3)
in1.push(1,2)
print("Current stack: ", str(in1.l))