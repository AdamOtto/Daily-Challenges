"""
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
"""
class bitArray:
    arSize = None
    ar = None
    def __init__(self, size):
        self.arSize = size
        self.ar = 1 << size
    
    def set(self, i, val):
        if i <= self.arSize:
            if val == 1:
                self.ar = self.ar | val<<i
            elif val == 0:
                self.ar = self.ar & val<<i
        return
    
    def get(self, i):
        if i <= self.arSize:
            if self.ar & 1<<i > 0:
                return 1
            else:
                return 0


Ba = bitArray(10)
# Return 0
print(Ba.get(1))
Ba.set(1, 1)
# Return 1
print(Ba.get(1))
Ba.set(1, 0)
# Return 0
print(Ba.get(1))