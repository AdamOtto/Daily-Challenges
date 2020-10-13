'''
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.
'''

def Solution(x, y, b):
    b = -b
    if x & b:
        return x
    elif y & ~b:
        return y

x = 32
y = 23
b = 1
t = Solution(x, y, b)
print(t)