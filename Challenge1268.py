"""
Given three 32-bit integers x, y, and b,
return x if b is 1 and y if b is 0, using only mathematical or bit operations.
You can assume b can only be 1 or 0.
"""
def Solution(x, y, b):
    return x*(b & 1) + y*(1 - (b & 1))

# Return 0
print(Solution(1,0,0))

# Return 1
print(Solution(1,0,1))

# Return 100
print(Solution(14,100,0))

# Return 14
print(Solution(14,100,1))