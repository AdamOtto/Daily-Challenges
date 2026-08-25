"""
Implement a 2D iterator class. It will be initialized with
an array of arrays, and should implement the following methods:

 - next(): returns the next element in the array of arrays.
   If there are no more elements, raise an exception.
 - has_next(): returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]],
calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""
class iterator:
    ar = None
    itr1 = None
    itr2 = None

    def __init__(self, arr):
        self.ar = arr
        self.itr1 = 0
        self.itr2 = 0

    def next(self):
        if not self.has_next():
            raise Exception("No more elements in array.")

        l1 = len(self.ar[self.itr1])

        if self.itr2 < l1:
            retVal = self.ar[self.itr1][self.itr2]
            self.itr2 += 1
            return retVal
        else:
            self.itr1 += 1
            self.itr2 = 0
            return self.next()

    def has_next(self):
        if self.itr1 + 1 < len(self.ar):
            return True
        else:
            l = len(self.ar[self.itr1])
            return l > self.itr2


# Print 1 2 3 4 5 6
in1 = [[1, 2], [3], [], [4, 5, 6]]
itr = iterator(in1)
while itr.has_next():
    print(itr.next())

# Print 100 200 300 400 500 600 700 800
in1 = [[100], [], [], [200,300,400], [], [500], [600,700], [], [], [],[],[800]]
itr = iterator(in1)
while itr.has_next():
    print(itr.next())