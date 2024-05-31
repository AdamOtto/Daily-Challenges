"""
Implement a data structure which carries out the following
operations without resizing the underlying array:

add(value): Add a value to the set of values.
check(value): Check whether a value is in the set.

The check method may return occasional false positives
(in other words, incorrectly identifying an element as part of the set),
but should always correctly identify a true element.
"""
class StaticArray:
    
    ar = None
    
    def __init__(self):
        self.ar = [0] * 16

    def add(self, value):
        temp = value
        i = 0
        while temp != 0:
            if temp & 1 == 1:
                self.ar[i] = 1
            temp >>= 1
            i += 1
    
    def check(self, value):
        count = 0
        for i in reversed(range(0, len(self.ar))):
            if self.ar[i] == 1 and count + pow(2, i) <= value:
                count += pow(2, i)
        if count == value:
            return True
        return False

in1 = StaticArray()
in1.add(4)
in1.add(8)
in1.add(200)
in1.add(400)

# Return all False
print("False Elements")
print(in1.check(1))
print(in1.check(56))
print(in1.check(17))
print(in1.check(255))

print()
# Return all True
print("False Positives")
print(in1.check(16))
print(in1.check(256))

print()
# Return all True
print("True Positives")
print(in1.check(200))
print(in1.check(400))