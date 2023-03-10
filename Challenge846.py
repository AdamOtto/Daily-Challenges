"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair)
returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
    
Implement car and cdr.
"""
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(p):
    def right(a, b):
        return a
    return p(right)

def cdr(p):
    def left(a, b):
        return b
    return p(left)

# Return 3
print( car(cons(3,4)) )

# Return 4
print( cdr(cons(3,4)) )