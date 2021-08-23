'''
Implement a data structure which carries out the following
operations without resizing the underlying array:

add(value): Add a value to the set of values.
check(value): Check whether a value is in the set.
The check method may return occasional false positives
(in other words, incorrectly identifying an element as part of the set),
but should always correctly identify a true element.

**Assumptions**
Values being added are integers.
'''

class MyStruct:
    
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
            

strut = MyStruct()
strut.add(1)
strut.add(8)
strut.add(424)
print("False elements")
print(strut.check(4))
print(strut.check(432))
print(strut.check(2))
print(strut.check(18))

print("False positives")
print(strut.check(9))
print(strut.check(425))

print("True positives")
print(strut.check(8))
print(strut.check(424))
