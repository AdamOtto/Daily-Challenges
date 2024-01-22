"""
Write a function, add_subtract, which alternately adds and subtracts curried arguments.
Here are some sample operations:

add_subtract(7) -> 7

add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0

add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11
"""
def Solution(ar, prev=None, count=None):
    if count == None:
        count = 0
    if prev == None:
        prev = ar
        return lambda x: Solution(x, prev, count)
    if ar == None:
        return prev

    if count % 2 == 0:
        prev = prev + ar
        return lambda x: Solution(x, prev, count + 1)
    else:
        prev = prev - ar
        return lambda x: Solution(x, prev, count + 1)


# Return 7
print(Solution(7)(None))
# Return 0
print(Solution(1)(2)(3)(None))
# Return 11
print(Solution(-5)(10)(3)(9)(None))