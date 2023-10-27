"""
Given an iterator with methods next() and hasNext(),
create a wrapper iterator, PeekableInterface, which also implements peek().
peek shows the next element that would be returned on next().

Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
"""

class PeekableInterface(object):
    it = None
    def __init__(self, iterator):
        self.it = iterator

    def peek(self):
        itCopy = PeekableInterface(self.it)
        return itCopy.next()

    def next(self):
        return self.it.next()

    def hasNext(self):
        return self.it.hasNext()