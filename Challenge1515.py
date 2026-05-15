"""
Given a list of numbers, create an algorithm that arranges
them in order to form the largest possible integer.

For example, given [10, 7, 76, 415], you should return 77641510.
"""
import functools
def Solution(ar):
    ar.sort(key=functools.cmp_to_key(Compare))
    ar.reverse()
  
    return "".join(map(str, ar))
    
def Compare(x, y):
    xy = x
    yx = y
    countx = county = 0
    while (x > 0):
        countx += 1
        x //= 10
    while (y > 0):
        county += 1
        y //= 10
    
    x = xy
    y = yx
    
    while (countx):
        countx -= 1
        yx *= 10
  
    while (county):
        county -= 1
        xy *= 10
    
    # Append x to y
    yx += x
  
    # Append y to x
    xy += y
  
    return 1 if xy > yx else -1
    
# Return 77641510
print(Solution([10, 7, 76, 415]))
# Return 98765432110
print(Solution([1,2,3,4,5,6,7,8,9,10]))