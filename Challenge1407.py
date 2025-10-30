"""
You are given an array representing the heights of neighboring buildings on a city street, from east to west.
The city assessor would like you to write an algorithm that returns how many of these buildings have a view
of the setting sun, in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3,
since the top floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?

*Assume numbers in input cannot be lower than 0
*I think the question has east and west confused, 3,7 and 8 would have an unobstructed view to the west.
"""

def Solution(ar):
    temp = -1
    l = len(ar)
    retVal = 0
    for i in range(l):
        if ar[i] > temp:
            retVal += 1
            temp = ar[i]
        
    return retVal


# Return 3
print(Solution([3, 7, 8, 3, 6, 1]))

# Return 4
print(Solution([1, 2, 3, 4]))

# Return 1
print(Solution([4, 3, 2, 1]))

# Return 3
print(Solution([3, 4, 3, 6, 2, 1, 2]))