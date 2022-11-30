"""
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""
class ChStack:
    d = None
    
    def __init__(self):
        self.d = []
    
    def push(self, val):
        self.d.append(val)
    
    def p0p(self):
        if len(self.d) > 0:
            return self.d.pop(-1)
        return None
    
    def max(self):
        return max(self.d)

in1 = ChStack()

# Return 3,2,1,None
for i in range(1,3 + 1):
    in1.push(i)
for i in range(1,4 + 1):
    print(in1.p0p())
    

# Return 5, 4
for i in range(1,6 + 1):
    in1.push(i)
in1.p0p()
print(in1.max())
in1.p0p()
print(in1.max())