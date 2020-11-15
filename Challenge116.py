"""
Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""
from random import *

class Node:

    def __init__(self,value,right = None, left = None):
        self.val = value
        self.r = right
        self.l = left

    def right(self):
        if self.r is None:
            self.r = Node(randint(0, 1))
            self.r_evaluated = True
        return self.r.val

    def left(self):
        if self.l is None:
            self.l = Node(randint(0, 1))
            self.l_evaluated = True
        return self.l.val

    def val(self):
        return self.val

def Generate():
    return Node(0)

t = Generate()

print(t.right())
print(t.left())

print(t.r.right())
print(t.r.left())

print(t.l.right())
print(t.l.left())