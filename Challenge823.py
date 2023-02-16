"""
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
"""

class bitArray:
    val = None
    size = None
    def __init__(self, Size):
        self.val = 0 << Size
        self.size = Size
    
    def set(self, i, val):
        if i <= self.size:
            if val == 1:
                self.val = self.val | val<<i
            elif val == 0:
                self.val = self.val & val<<i
        return
    
    def get(self, i):
        if i <= self.size:
            if self.val & 1<<i > 0:
                return 1
            else:
                return 0


ar = bitArray(10)
ar.set(3, 1)
# Return 1
print(ar.get(3))
# Return 0
print(ar.get(7))
ar.set(3, 0)
# Return 0
print(ar.get(3))

# return None
ar.set(20, 1)
print(ar.get(20))