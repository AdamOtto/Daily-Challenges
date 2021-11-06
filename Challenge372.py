"""
Write a function that takes a natural number as
input and returns the number of digits the input has.
"""

def Solution(ar):
    if ar <= 0:
        return None
    if ar < 10:
        return 1
    
    i = 10
    count = 2
    while i <= ar:
        i *= 10
        count += 1
    return count - 1
    
# Return 4
in1 = 1234
print(Solution(in1))

# Return 3
in1 = 100
print(Solution(in1))

# Return 5
in1 = 14441
print(Solution(in1))