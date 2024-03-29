"""
reduce (also known as fold) is a function that takes in an array,
a combining function, and an initial value and builds up a result by
calling the combining function on each element of the array, left to right.
For example, we can write sum() in terms of reduce:
def add(a, b):
    return a + b
def sum(lst):
    return reduce(lst, add, 0)
    
This should call add on the initial value with the first element of the array,
and then the result of that with the second element of the array,
and so on until we reach the end, when we return the sum of the array.
Implement your own version of reduce.
"""
def add(a, b):
    return a + b

def sum(lst):
    return reduce(lst, add, 0)

def reduce(lst, add, cur):
    if len(lst) == 0:
        return cur
    temp = lst.pop(0)
    return reduce(lst, add, add(cur, temp))

# Return 15
print(sum([1,2,3,4,5]))
# Return 6
print(sum([1,0,2,0,3]))