"""
You are given an array representing the heights of neighboring
buildings on a city street, from west to east.
The city assessor would like you to write an algorithm that
returns how many of these buildings have a view of the rising sun,
in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3,
since the top floors of the buildings with heights 8, 6, and 1
all have an unobstructed view to the east.

Can you do this using just one forward pass through the array?
"""

def Solution(ar):
    l = len(ar)
    highest = 0
    count = 0
    for i in reversed(range(l)):
        if ar[i] > highest:
            count += 1
            highest = ar[i]
    return count

# Return 3
print(Solution([3,7,8,3,6,1]))

# Return 1
print(Solution([1,2,3,4,1,2,3,4]))

# Return 7
print(Solution([7,8,6,5,4,3,2,1]))